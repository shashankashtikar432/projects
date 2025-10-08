# RHEL 10 build server image
FROM redhat/ubi10
RUN echo "Building RHEL 10 build server image using official redhat UBI 10"
LABEL maintainer=DevOpsTeam
# Install essential tools and libraries
RUN echo "Install essentials"
RUN dnf install -y python3 git gcc-c++ make cmake sudo which findutils curl java-21-openjdk-devel

# RUN microdnf install -y dnf
RUN ln -s /usr/bin/python3 /usr/local/bin/python
RUN groupadd buildgroup; \
    useradd -g buildgroup -G root builduser;

# Set up workdir for the image
WORKDIR /

# Create a directory structure for the build image.
# Cleanup
RUN rm -rf /build

# Create directory structure
RUN mkdir /build; \
    mkdir /build/jenkins; \
    mkdir /build/buildtools; \
    mkdir /build/package; \
    mkdir /build/buildtools/bin

# Change ownership of the build directory and files under it.
# RUN chown -R builduser:buildgroup /build

# Change to build user
# USER builduser

# Copy build tools and jenkins setup
COPY buildtools /build/buildtools
COPY jenkins /build/jenkins
RUN chmod -R u+x /build/jenkins/check_image.sh; \
    chmod -R u+x /build/jenkins/check_image.py;

# Extract build tools
WORKDIR /build/buildtools
RUN tar xzf /build/buildtools/apache-ant-1.10.15-bin.tar.gz; \
    mv apache-ant-1.10.15 apache-ant; \
    ln -s /build/buildtools/apache-maven/bin/mvn /build/buildtools/bin/mvn; 
RUN tar xzf /build/buildtools/apache-maven-3.9.11-bin.tar.gz; \
    mv apache-maven-3.9.11 apache-maven; \
    ln -s /build/buildtools/apache-ant/bin/ant /build/buildtools/bin/ant;
RUN tar xzf /build/buildtools/cmake-4.1.2-linux-x86_64.tar.gz; \
    mv cmake-4.1.2-linux-x86_64 cmake; \
    ln -s /build/buildtools/cmake/bin/cmake /build/buildtools/bin/cmake;

# Setup PATH environment variable for build tools
ENV PATH="/build/buildtools/bin:${PATH}"
ENV JAVA_HOME=/usr/lib/jvm/java-openjdk

WORKDIR  /build/jenkins
RUN python3 -m venv /build/jenkins/pythonvenv
RUN source /build/jenkins/pythonvenv/bin/activate; \
    pip install --upgrade pip; \
    pip install -r /build/jenkins/requirements.txt;

# Add jenkins client to the image
ADD http://thing:8080/jnlpJars/jenkins-cli.jar /build/jenkins/jenkins-cli.jar

# HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD ["/build/jenkins/check_image.sh"]
HEALTHCHECK CMD ["/build/jenkins/check_image.sh"]
# CMD [ "java", "-jar", "jenkins-cli.jar"]
