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

    new ApplicationLoadBalancedFargateService(
      this,
      'streamlitApp',
      {
        desiredCount: 1,
        domainZone: hostedZone,
        listenerPort: 8051,
        taskImageOptions: {
          image: ecs.ContainerImage.fromEcrRepository(ecrRepo),
          containerName: 'StreamlitApp',
          containerPort: 8051
        }
      }
      )
  }
}
