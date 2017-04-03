FROM martsime/dsscdb:latest
RUN apt-get update
ENV PYTHONUNBUFFERED 1
ENV PATH /opt/conda/envs/rdkitenv/bin:$PATH

RUN mkdir /code
COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt
COPY . /code/
RUN chmod +x /code/entrypoint.sh
#CMD ["/bin/bash","-c", "/code/entrypoint.sh"]
CMD ["/bin/bash"]

