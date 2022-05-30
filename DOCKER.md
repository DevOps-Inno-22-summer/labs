# DevOps

## Docker build and run
```
docker image build -t devopslab .
docker run -p 5001:5000 -d devopslab
```

## Best Practices
1. Use .dockerignore 
2. Use small base images. Avoid distro bases
3. Add non-root user
4. Use EXPOSE to document ports that you need to make app accessible
5. COPY instead of ADD if possible