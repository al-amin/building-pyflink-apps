FROM flink:1.17.1
ARG PYTHON_VERSION
ARG FLINK_VERSION

# Versions
ENV \
  # Apt-Get
  BUILD_ESSENTIAL_VER=12.9ubuntu3 \
  JDK_VER=11.0.20.1+1-0ubuntu1~22.04 \
  LIBBZ2_DEV_VER=1.0.8-5build1 \
  LIBFFI_DEV_VER=3.4.2-4 \
  LIBSSL_DEV_VER=3.0.2-0ubuntu1.10 \
  ZLIB1G_DEV_VER=1:1.2.11.dfsg-2ubuntu9.2 \
  # Python
  PYTHON_VERSION=3.10.13 \
  # PyFlink
  FLINK_VERSION=1.17.1
  
SHELL ["/bin/bash", "-ceuxo", "pipefail"]

RUN apt-get update -y && \
  apt-get install -y --no-install-recommends \
    build-essential libssl-dev zlib1g-dev libbz2-dev libffi-dev liblzma-dev \
    openjdk-11-jdk-headless \
    # libbz2-dev=${LIBBZ2_DEV_VER} \
    # libffi-dev=${LIBFFI_DEV_VER} \
    # libssl-dev=${LIBSSL_DEV_VER} \
    # zlib1g-dev=${ZLIB1G_DEV_VER} \
  && \
  wget -q "https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tar.xz" && \
  tar -xf "Python-${PYTHON_VERSION}.tar.xz" && \
  cd "Python-${PYTHON_VERSION}" && \
  ./configure --enable-optimizations --without-tests --enable-shared && \
  make -j$(nproc) && \
  make install && \
  ldconfig /usr/local/lib && \
  cd .. && \
  rm -rf "Python-${PYTHON_VERSION}" "Python-${PYTHON_VERSION}.tar.xz" && \
  ln -s /usr/local/bin/python3 /usr/local/bin/python && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

# Installing OpenJDK again & setting this is required due to a bug with M1 Macs
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-arm64

RUN pip3 install --no-cache-dir apache-flink==${FLINK_VERSION} && \
  pip3 cache purge

# USER flink
# RUN mkdir /opt/flink/usrlib
# COPY python_demo.py /opt/flink/usrlib/python_demo.py

RUN wget -P /opt/flink/lib/ https://repo.maven.apache.org/maven2/org/apache/flink/flink-connector-kafka/$FLINK_VERSION/flink-connector-kafka-$FLINK_VERSION.jar; \
  wget -P /opt/flink/lib/ https://repo.maven.apache.org/maven2/org/apache/kafka/kafka-clients/3.2.3/kafka-clients-3.2.3.jar; \
  wget -P /opt/flink/lib/ https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-connector-kafka/$FLINK_VERSION/flink-sql-connector-kafka-$FLINK_VERSION.jar; \
  wget -P /opt/flink/lib/ https://github.com/knaufk/flink-faker/releases/download/v0.5.3/flink-faker-0.5.3.jar;

