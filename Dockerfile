FROM alpine:3.9
ARG MONITOROR_VERSION=4.0.1

ADD https://github.com/monitoror/monitoror/releases/download/${MONITOROR_VERSION}/monitoror-linux-amd64-${MONITOROR_VERSION} /monitoror
RUN chmod +x /monitoror
ENTRYPOINT [ "/monitoror" ]
EXPOSE 8080
