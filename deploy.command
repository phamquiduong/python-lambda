# Remove packages folder
rm -r cdk/layer/packages/

# Build layer
docker build . -t python_layer -f cdk/layer/Dockerfile
docker run --name python_layer python_layer
docker cp python_layer:/packages ./cdk/layer/packages

# Deploy code
cd cdk/
cdk deploy -y
