# IMAGE NAME IN PROJECT
# getting-started

FROM node:12-alpine
# An alternative base image
# FROM countingup/node

RUN apk add --no-cache python2 g++ make
WORKDIR /app
COPY . .
RUN yarn install --production
CMD ["node", "src/index.js"]
EXPOSE 3000
