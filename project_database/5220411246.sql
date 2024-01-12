-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 12, 2024 at 05:24 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5220411246`
--

-- --------------------------------------------------------

--
-- Table structure for table `tb_dsn`
--

CREATE TABLE `tb_dsn` (
  `nidn` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `mata_kuliah` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_dsn`
--

INSERT INTO `tb_dsn` (`nidn`, `nama`, `mata_kuliah`) VALUES
(1, 'Dosen 1', 'Pemrograman Berorientasi Objek Praktik'),
(2, 'Dosen 2', 'Algoritma Pemrograman'),
(3, 'Dosen 3', 'Web Praktik'),
(4, 'Dosen 4', 'Kecerdasan Buatan'),
(5, 'Dosen 1', 'Pengantar Analisis Data');

-- --------------------------------------------------------

--
-- Table structure for table `tb_mhs`
--

CREATE TABLE `tb_mhs` (
  `npm` int(11) NOT NULL,
  `nama` varchar(255) DEFAULT NULL,
  `jurusan` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_mhs`
--

INSERT INTO `tb_mhs` (`npm`, `nama`, `jurusan`) VALUES
(1, 'Mahasiswa 1', 'Informatika'),
(2, 'Mahasiswa 2', 'Informatika'),
(3, 'Mahasiswa 3', 'Informatika'),
(4, 'Mahasiswa 4', 'Informatika'),
(5, 'Mahasiswa 5', 'Informatika');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_dsn`
--
ALTER TABLE `tb_dsn`
  ADD PRIMARY KEY (`nidn`);

--
-- Indexes for table `tb_mhs`
--
ALTER TABLE `tb_mhs`
  ADD PRIMARY KEY (`npm`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
