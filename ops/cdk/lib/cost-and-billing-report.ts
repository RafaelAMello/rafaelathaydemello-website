import * as cdk from '@aws-cdk/core'
import * as s3 from '@aws-cdk/aws-s3'
import * as iam from '@aws-cdk/aws-iam'
import * as cur from '@aws-cdk/aws-cur'

export class CostAndBillingReport extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props)
    const bucket = new s3.Bucket(this, 'CostAndBillingReportBucket', {
        bucketName: `cost-and-billing-bucket-${this.account}`,
    })

    bucket.grantReadWrite(new iam.ServicePrincipal('billingreports.amazonaws.com'))

    new cur.CfnReportDefinition(this, 'CostAndBillingReport', {
      reportName: 'regular-cost-usage-report',
      compression: 'gzip',
      format: 'parquet',
      refreshClosedReports: true,
      reportVersioning: 'OVERWRITE_REPORT',
      timeUnit: 'Daily',
      s3Bucket: bucket.bucketArn,
      s3Prefix: 'reports',
      s3Region: this.region
    })
  }
}
