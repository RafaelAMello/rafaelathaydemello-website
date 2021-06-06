FROM node:14.15.4-alpine

WORKDIR /opt/code

# Install depenedncies
COPY package.json yarn.lock ./
RUN yarn install

COPY . .
CMD yarn run cdk deploy --require-approval never --verbose
