CREATE TABLE IF NOT EXISTS `biblioteca`.`usuariotb` (
  `ID_usuario` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(50) NOT NULL,
  `password` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`ID_usuario`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `biblioteca`.`leitortb` (
  `ID_leittor` INT NOT NULL AUTO_INCREMENT,
  `cpf` CHAR(11) NOT NULL,
  `nome` VARCHAR(100) NOT NULL,
  `telefone` VARCHAR(20) NULL,
  `email` VARCHAR(50) NULL,
  PRIMARY KEY (`ID_leittor`),
  UNIQUE INDEX `CPF_UNIQUE` (`cpf` ASC) VISIBLE)
ENGINE = InnoDB

CREATE TABLE IF NOT EXISTS `biblioteca`.`livrotb` (
  `ID_livro` INT NOT NULL AUTO_INCREMENT,
  `isbn` CHAR(13) NOT NULL,
  `titulo` VARCHAR(150) NOT NULL,
  `autor` VARCHAR(100) NOT NULL,
  `genero` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`ID_livro`),
  UNIQUE INDEX `isbn_UNIQUE` (`isbn` ASC) VISIBLE)
ENGINE = InnoDB

CREATE TABLE IF NOT EXISTS `biblioteca`.`emprestimotb` (
  `ID_leitor` INT NOT NULL,
  `ID_livro` INT NOT NULL,
  `data_inicio` DATE NOT NULL,
  `total_dias` INT NOT NULL,
  `data_retorno` DATE NULL,
  INDEX `fk_emprestimotb_leitortb_idx` (`ID_leitor` ASC) VISIBLE,
  INDEX `fk_emprestimotb_livrotb1_idx` (`ID_livro` ASC) VISIBLE,
  PRIMARY KEY (`ID_leitor`, `ID_livro`, `data_inicio`),
  CONSTRAINT `fk_emprestimotb_leitortb`
    FOREIGN KEY (`ID_leitor`)
    REFERENCES `biblioteca`.`leitortb` (`ID_leittor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_emprestimotb_livrotb1`
    FOREIGN KEY (`ID_livro`)
    REFERENCES `biblioteca`.`livrotb` (`ID_livro`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB

CREATE TABLE IF NOT EXISTS `biblioteca`.`estoquetb` (
  `ID_estoque` INT NOT NULL AUTO_INCREMENT,
  `ID_livro` INT NOT NULL,
  `quantidade` INT NOT NULL,
  INDEX `fk_estoquetb_livrotb1_idx` (`ID_livro` ASC) VISIBLE,
  PRIMARY KEY (`ID_estoque`),
  UNIQUE INDEX `ID_livro_UNIQUE` (`ID_livro` ASC) VISIBLE,
  CONSTRAINT `fk_estoquetb_livrotb1`
    FOREIGN KEY (`ID_livro`)
    REFERENCES `biblioteca`.`livrotb` (`ID_livro`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB

INSERT INTO usuariotb (username, password) VALUES ('a', 'a')

SELECT * FROM usuariotb