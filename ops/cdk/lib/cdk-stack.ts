import * as cdk from '@aws-cdk/core'
import * as ecs from '@aws-cdk/aws-ecs'
import * as ecr from '@aws-cdk/aws-ecr'
import * as route53 from '@aws-cdk/aws-route53'
import * as route53_targets from '@aws-cdk/aws-route53-targets'
import { ApplicationLoadBalancedFargateService } from '@aws-cdk/aws-ecs-patterns'

const REPO_NAME = 'personal-website/streamlit'
interface StreamlitAppProps extends cdk.StackProps {
  imageTag: string
}

export class StreamlitApp extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props: StreamlitAppProps) {
    super(scope, id, props)

    const ecrRepo = ecr.Repository.fromRepositoryName(this, 'StreamlitRepo', REPO_NAME)
    const hostedZone = route53.HostedZone.fromLookup(this, 'HostedZone', { domainName: 'rafaelathaydemello.com' })

    const app = new ApplicationLoadBalancedFargateService(
      this,
      'streamlitApp',
      {
        desiredCount: 1,
        minHealthyPercent: 0,
        domainZone: hostedZone,
        taskImageOptions: {
          image: ecs.ContainerImage.fromEcrRepository(ecrRepo, props.imageTag),
          containerName: 'StreamlitApp',
          containerPort: 8501
        }
      })

      new route53.RecordSet(this, 'recordSet', {
          recordType: route53.RecordType.A,
          target: route53.RecordTarget.fromAlias(new route53_targets.LoadBalancerTarget(app.loadBalancer)),
          zone: hostedZone,
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
