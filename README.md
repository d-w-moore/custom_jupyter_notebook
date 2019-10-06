# Custom Jupyter Notebook

Build the image

```
docker build --build-arg=notebook_{pw="hello",port=8889} -t mynotebook . --no-cache
```

Run it:

```
docker run  -dit -p8889:8889 mynotebook
```

Navigate to localhost:8889 . Enter the password, "hello", when prompted.
