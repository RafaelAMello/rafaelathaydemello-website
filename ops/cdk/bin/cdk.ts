#!/usr/bin/env node
import 'source-map-support/register'
import * as cdk from '@aws-cdk/core'
import { StreamlitApp, StreamlitEcr } from '../lib/cdk-stack'

const app = new cdk.App()
new StreamlitEcr(app, 'StreamlitEcr')
new StreamlitApp(app, 'StreamlitApp', {
    env: {
        account: process.env['CDK_DEFAULT_ACCOUNT'],
        region: process.env['CDK_DEFAULT_REGION'],
    },
    imageTag: process.env['GITHUB_RUN_ID'] || 'latest',
})
