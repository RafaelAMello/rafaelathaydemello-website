import * as cdk from '@aws-cdk/core'
import * as ecs from '@aws-cdk/aws-ecs'
import * as ecr from '@aws-cdk/aws-ecr'
import * as ec2 from '@aws-cdk/aws-ec2'
import * as ssm from '@aws-cdk/aws-ssm'
import * as route53 from '@aws-cdk/aws-route53'
import * as route53_targets from '@aws-cdk/aws-route53-targets'
import * as certificatemanager from '@aws-cdk/aws-certificatemanager'
import { ApplicationLoadBalancedFargateService } from '@aws-cdk/aws-ecs-patterns'

const REPO_NAME = 'personal-website/streamlit'
interface StreamlitAppProps extends cdk.StackProps {
  imageTag: string
}

export class StreamlitApp extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props: StreamlitAppProps) {
    super(scope, id, props)

    const domainName = 'rafaelathaydemello.com'

    const ecrRepo = ecr.Repository.fromRepositoryName(this, 'StreamlitRepo', REPO_NAME)
    const hostedZone = route53.HostedZone.fromLookup(this, 'HostedZone', { domainName: domainName })
    const cert = new certificatemanager.DnsValidatedCertificate(this, 'cert', {
      domainName: domainName,
      hostedZone: hostedZone,
    })

    const webhookUrlSecret = ecs.Secret.fromSsmParameter(
        new ssm.StringParameter(this, 'SlackWebhookURL', {
          parameterName: 'slackWebhookUrl',
          stringValue: 'https://hooks.slack.com/services/1111/111/111',
        })
    )

    const app = new ApplicationLoadBalancedFargateService(
      this,
      'streamlitApp',
      {
        desiredCount: 1,
        minHealthyPercent: 0,
        domainZone: hostedZone,
        certificate: cert,
        redirectHTTP: true,
        taskImageOptions: {
          image: ecs.ContainerImage.fromEcrRepository(ecrRepo, props.imageTag),
          containerName: 'StreamlitApp',
          containerPort: 8501,
          secrets: {
            'SLACK_URL' : webhookUrlSecret
          }
        },
        taskSubnets: {
          subnetType: ec2.SubnetType.PUBLIC
        }
      })

      if (app.taskDefinition.executionRole === undefined) {
        throw new Error("Execution role needs to be defined")
      }

      webhookUrlSecret.grantRead(app.taskDefinition.executionRole)

      new route53.RecordSet(this, 'recordSet', {
          recordType: route53.RecordType.A,
          target: route53.RecordTarget.fromAlias(new route53_targets.LoadBalancerTarget(app.loadBalancer)),
          zone: hostedZone,
        })

      new ssm.StringParameter(this, 'EcsClusterName', {
        parameterName: 'EcsClusterName',
        stringValue: app.cluster.clusterName,
      })

      new ssm.StringParameter(this, 'EcsServiceName', {
        parameterName: 'EcsServiceName',
        stringValue: app.service.serviceName,
      })
  }
}

export class StreamlitEcr extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)

    new ecr.Repository(this, 'streamlitECR', {
      repositoryName: REPO_NAME,
      lifecycleRules: [{
        maxImageCount: 1,
        description: "Retain only the latest images",
      }]
    })

  }
}
