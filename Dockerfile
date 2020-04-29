FROM python

RUN apt-get update && \
	apt-get install -y \
		curl \
		libfreetype6 \
		libglu1-mesa \
		libxi6 \
		libxrender1 \
		xz-utils && \
	apt-get -y autoremove && \
	rm -rf /var/lib/apt/lists/*

ENV BLENDER_MAJOR 2.82
ENV BLENDER_VERSION 2.82a
ENV BLENDER_URL https://download.blender.org/release/Blender${BLENDER_MAJOR}/blender-${BLENDER_VERSION}-linux64.tar.xz

RUN curl -L ${BLENDER_URL} | tar -xJ -C /usr/local/ && \
	mv /usr/local/blender-${BLENDER_VERSION}-linux64 /usr/local/blender

ENV APP_HOME /app
COPY . $APP_HOME
WORKDIR $APP_HOME

RUN pip install Flask
CMD ["python", "invoker.py"]