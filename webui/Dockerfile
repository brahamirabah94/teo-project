FROM node:alpine
WORKDIR /usr/app
COPY ./ ./
RUN npm install express && \
    npm install redis
EXPOSE 80
CMD [ "node", "webui.js" ]
