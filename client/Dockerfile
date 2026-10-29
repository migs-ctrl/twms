# build stage
FROM node as builder
WORKDIR /app
COPY package*.json ./
RUN npm install
RUN npm instal @vue/compat
RUN npm install @vue/composition-api --force
RUN npm install pinia --legacy-peer-deps
COPY . .
RUN npm run build

# Step 2: Set up the production environment
FROM nginx:stable-alpine
COPY --from=builder /app/dist/ /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]