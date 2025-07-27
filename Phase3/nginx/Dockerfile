# Use official Nginx image as base
FROM nginx:alpine

# Remove default config
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom nginx.conf into the container
COPY nginx.conf /etc/nginx/nginx.conf
