FROM ruby:3-alpine
RUN apk add --update build-base curl && \
    gem install sinatra && \
    gem install thin
ADD hasher.rb /
EXPOSE 80
CMD ["ruby", "hasher.rb"]
