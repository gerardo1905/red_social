
CREATE TABLE usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  correo VARCHAR(150) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
  estado ENUM('activo','inactivo') DEFAULT 'activo'
);

CREATE TABLE amistad (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_usuario_1 INT NOT NULL,
  id_usuario_2 INT NOT NULL,
  estado ENUM('pendiente','aceptada','bloqueada') DEFAULT 'pendiente',
  fecha_inicio DATETIME DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_amistad_usuario1 FOREIGN KEY (id_usuario_1) REFERENCES usuarios(id),
  CONSTRAINT fk_amistad_usuario2 FOREIGN KEY (id_usuario_2) REFERENCES usuarios(id)
);

CREATE TABLE publicaciones (
  id INT AUTO_INCREMENT PRIMARY KEY,
  contenido TEXT NOT NULL,
  fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
  id_autor INT NOT NULL,
  tipo ENUM('texto','imagen','video') DEFAULT 'texto',
  CONSTRAINT fk_pub_autor FOREIGN KEY (id_autor) REFERENCES usuarios(id)
);

CREATE TABLE likes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_publicacion INT NOT NULL,
  id_usuario INT NOT NULL,
  fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_like_pub FOREIGN KEY (id_publicacion) REFERENCES publicaciones(id),
  CONSTRAINT fk_like_user FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
  UNIQUE (id_publicacion, id_usuario)
);

CREATE TABLE comentarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_publicacion INT NOT NULL,
  id_autor INT NOT NULL,
  texto TEXT NOT NULL,
  fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_com_pub FOREIGN KEY (id_publicacion) REFERENCES publicaciones(id),
  CONSTRAINT fk_com_user FOREIGN KEY (id_autor) REFERENCES usuarios(id)
);

CREATE TABLE mensajes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  contenido TEXT NOT NULL,
  fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
  id_emisor INT NOT NULL,
  id_receptor INT NOT NULL,
  leido BOOLEAN DEFAULT FALSE,
  CONSTRAINT fk_msg_emisor FOREIGN KEY (id_emisor) REFERENCES usuarios(id),
  CONSTRAINT fk_msg_receptor FOREIGN KEY (id_receptor) REFERENCES usuarios(id)
);
