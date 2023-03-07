FROM node:16.15.0 AS builder
CMD echo "hello"
ADD ./frontend/package.json /frontend/package.json
WORKDIR /frontend
RUN yarn install
ADD ./frontend /frontend
RUN yarn build --base="/routes/yolo_faces/web/"

FROM python:3.10-slim
EXPOSE 8080
RUN apt-get update --fix-missing && apt-get install -y libgl1 libglib2.0-0 libsm6 libxrender1 libxext6
ADD ./requirements.lock /
RUN pip install -r /requirements.lock
ARG GATEWAY
ENV GATEWAY=$GATEWAY
ADD . /plugin
COPY --from=builder /frontend/dist /frontend/dist
ENV PYTHONPATH=$PYTHONPATH:/plugin
WORKDIR /plugin/services
CMD python services.py