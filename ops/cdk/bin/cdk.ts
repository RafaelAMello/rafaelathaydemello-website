#!/usr/bin/env node
import 'source-map-support/register'
import * as cdk from '@aws-cdk/core'

import { StreamlitApp, StreamlitEcr } from '../lib/cdk-stack'
import { CostAndBillingReport } from '../lib/cost-and-billing-report'

const getEnvVariable = (envVarName: string): string => {
    const envVar = process.env[envVarName]
    if (envVar === undefined) {
        throw new Error(`${envVarName} Variables not set`)
    }
    return envVar
}

const app = new cdk.App()
new StreamlitEcr(app, 'StreamlitEcr')
new StreamlitApp(app, 'StreamlitApp', {
    env: {
        account: getEnvVariable('CDK_DEFAULT_ACCOUNT'),
        region: getEnvVariable('CDK_DEFAULT_REGION'),
    },
    imageTag: getEnvVariable('GITHUB_RUN_ID')
})
new CostAndBillingReport(app, 'CostAndBillingReport')
