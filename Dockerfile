FROM jupyter/base-notebook

ARG notebook_pw="notebook"

ARG notebook_ip="0.0.0.0"
ENV NOTEBOOK_IP=$notebook_ip

ARG notebook_port=8888
ENV NOTEBOOK_PORT=$notebook_port

COPY modify_json_config.py /tmp

RUN python /tmp/modify_json_config.py "$notebook_pw"

CMD jupyter notebook --no-browser --ip=${NOTEBOOK_IP} --port=${NOTEBOOK_PORT}
