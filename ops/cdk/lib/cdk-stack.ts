import * as cdk from '@aws-cdk/core'
import * as ecs from '@aws-cdk/aws-ecs'
import * as ecr from '@aws-cdk/aws-ecr'
import * as route53 from '@aws-cdk/aws-route53'
import { ApplicationLoadBalancedFargateService } from '@aws-cdk/aws-ecs-patterns'

export class StreamlitApp extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)

    const ecrRepo = ecr.Repository.fromRepositoryName(this, 'StreamlitRepo', 'personal-website/streamlit-app')
    const hostedZone = route53.HostedZone.fromHostedZoneId(this, 'HostedZone', 'Z03972782S02DJS3QFINK')

    const app = new ApplicationLoadBalancedFargateService(
      this,
      'streamlitApp',
      {
        desiredCount: 1,
        domainZone: hostedZone,
        taskImageOptions: {
          image: ecs.ContainerImage.fromEcrRepository(ecrRepo),
          containerName: 'StreamlitApp',
          containerPort: 8501
        }
      }
      )
      new route53.RecordSet(this, 'recordSet', {
          recordType: route53.RecordType.A,
          target: route53.RecordTarget.fromIpAddresses(app.loadBalancer.loadBalancerDnsName),
          zone: hostedZone,
        }
        )
  }
}

export class StreamlitEcr extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)

    new ecr.Repository(this, 'streamlitECR', {
      repositoryName: 'personal-website/streamlit',
      lifecycleRules: [{
        maxImageCount: 1,
        description: "Retain the 50 latest images",
      }]
    })

  }
}
