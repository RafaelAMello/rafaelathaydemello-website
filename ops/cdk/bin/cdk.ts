#!/usr/bin/env node
import 'source-map-support/register'
import * as cdk from '@aws-cdk/core'
import { StreamlitApp, StreamlitEcr } from '../lib/cdk-stack'

const app = new cdk.App()
new StreamlitEcr(app, 'StreamlitEcr')
new StreamlitApp(app, 'StreamlitApp')
