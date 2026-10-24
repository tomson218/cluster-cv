FROM node:26-alpine
WORKDIR /app

# Zainstaluj pnpm w kontenerze
RUN npm install -g pnpm

# Skopiuj pliki manifestu i lockfile
COPY package.json pnpm-lock.yaml ./

# Zainstaluj zależności za pomocą pnpm
RUN pnpm install

COPY . .
CMD ["pnpm", "dev", "--host", "0.0.0.0"]