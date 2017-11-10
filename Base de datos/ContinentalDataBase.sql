SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Continente`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `mydb`.`Continente` (
  `Codigo` INT NOT NULL ,
  `Nombre` VARCHAR(45) NOT NULL ,
  `Coordenada W` VARCHAR(15) NULL ,
  `Coordenada S` VARCHAR(15) NULL ,
  PRIMARY KEY (`Codigo`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Pais`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `mydb`.`Pais` (
  `Codigo` INT NOT NULL ,
  `Nombre` VARCHAR(45) NOT NULL ,
  `Coordenada W` VARCHAR(15) NULL ,
  `Coordenada S` VARCHAR(15) NULL ,
  `Continente_Codigo` INT NOT NULL ,
  PRIMARY KEY (`Codigo`, `Continente_Codigo`) ,
  INDEX `fk_Pais_Continente_idx` (`Continente_Codigo` ASC) ,
  CONSTRAINT `fk_Pais_Continente`
    FOREIGN KEY (`Continente_Codigo` )
    REFERENCES `mydb`.`Continente` (`Codigo` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`ProvinciaEstado`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `mydb`.`ProvinciaEstado` (
  `Codigo` INT NOT NULL ,
  `Nombre` VARCHAR(45) NOT NULL ,
  `Coordenada W` VARCHAR(15) NULL ,
  `Coordenada S` VARCHAR(15) NULL ,
  `Pais_Codigo` INT NOT NULL ,
  PRIMARY KEY (`Codigo`, `Pais_Codigo`) ,
  INDEX `fk_ProvinciaEstado_Pais1_idx` (`Pais_Codigo` ASC) ,
  CONSTRAINT `fk_ProvinciaEstado_Pais1`
    FOREIGN KEY (`Pais_Codigo` )
    REFERENCES `mydb`.`Pais` (`Codigo` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Ciudad`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `mydb`.`Ciudad` (
  `Codigo` INT NOT NULL ,
  `Nombre` VARCHAR(45) NOT NULL ,
  `Coordenada W` VARCHAR(15) NULL ,
  `Coordenada S` VARCHAR(15) NULL ,
  `ProvinciaEstado_Codigo` INT NOT NULL ,
  PRIMARY KEY (`Codigo`, `ProvinciaEstado_Codigo`) ,
  INDEX `fk_Ciudad_ProvinciaEstado1_idx` (`ProvinciaEstado_Codigo` ASC) ,
  CONSTRAINT `fk_Ciudad_ProvinciaEstado1`
    FOREIGN KEY (`ProvinciaEstado_Codigo` )
    REFERENCES `mydb`.`ProvinciaEstado` (`Codigo` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Barrio`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `mydb`.`Barrio` (
  `Codigo` INT NOT NULL ,
  `Nombre` VARCHAR(45) NOT NULL ,
  `Coordenada W` VARCHAR(15) NULL ,
  `Coordenada S` VARCHAR(15) NULL ,
  `Poblacion` INT NULL ,
  `Ciudad_Codigo` INT NOT NULL ,
  PRIMARY KEY (`Codigo`, `Ciudad_Codigo`) ,
  INDEX `fk_Barrio_Ciudad1_idx` (`Ciudad_Codigo` ASC) ,
  CONSTRAINT `fk_Barrio_Ciudad1`
    FOREIGN KEY (`Ciudad_Codigo` )
    REFERENCES `mydb`.`Ciudad` (`Codigo` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `mydb` ;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
