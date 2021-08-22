-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 25, 2020 at 08:20 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `covid`
--

-- --------------------------------------------------------

--
-- Table structure for table `labs`
--

CREATE TABLE `labs` (
  `id` int(100) NOT NULL,
  `name` varchar(255) NOT NULL,
  `labid` varchar(100) NOT NULL,
  `tel` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `branch` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `phis`
--

CREATE TABLE `phis` (
  `id` int(100) NOT NULL,
  `phi_name` varchar(255) NOT NULL,
  `phi_id` varchar(255) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `address` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `tel` varchar(20) NOT NULL,
  `phi_division` varchar(255) NOT NULL,
  `date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `phis`
--

INSERT INTO `phis` (`id`, `phi_name`, `phi_id`, `gender`, `address`, `email`, `tel`, `phi_division`, `date`) VALUES
(1, 'test', '21', '1', 'dambewatana', 'yyusb@gmail.com', '2641961548', 'Anuradhapura', '2020-03-21 00:00:00.000000');

-- --------------------------------------------------------

--
-- Table structure for table `pns`
--

CREATE TABLE `pns` (
  `id` int(100) NOT NULL,
  `user_id` varchar(255) NOT NULL,
  `level` varchar(255) NOT NULL,
  `division` varchar(100) NOT NULL,
  `date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pns`
--

INSERT INTO `pns` (`id`, `user_id`, `level`, `division`, `date`) VALUES
(1, '4160', '1', 'anuradhapura', '2020-11-30 00:00:00.000000'),
(2, '45', '0', 'anuradhapura', '2020-12-03 00:00:00.000000'),
(3, '45', '0', 'anuradhapura', '2020-12-03 00:00:00.000000'),
(4, '45841116', '1', 'anurdhapura', '2020-12-24 00:00:00.000000');

-- --------------------------------------------------------

--
-- Table structure for table `reports`
--

CREATE TABLE `reports` (
  `id` int(100) NOT NULL,
  `user_id` varchar(255) NOT NULL,
  `parth` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(100) NOT NULL,
  `name` varchar(255) NOT NULL,
  `age` varchar(255) NOT NULL,
  `nic` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `division` varchar(255) NOT NULL,
  `tel` varchar(255) NOT NULL,
  `date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `name`, `age`, `nic`, `gender`, `address`, `email`, `division`, `tel`, `date`) VALUES
(2, 'John', '24', '456879542', 'male', 'Highway 21', 'john@gmail.com', 'Anuradhapura', 'Aruna', '2020-12-21 00:00:00.000000'),
(3, 'test', 'test', 'test', 'test', 'test', 'test', 'test', 'test', '0202-03-21 00:00:00.000000'),
(4, 'Dilum', '21', '456879568v', '', 'Aluth Dambewatana', 'dilum@gmail.com', 'Anuradhapura', '1254789865', '2020-12-25 00:00:00.000000'),
(5, 'dilum', '21', '125479564v', '', 'dambewatana', 'dilum@g.com', 'anuradhapura', '4587968534', '2020-03-20 00:00:00.000000'),
(6, 'ds', '25', '457895435v', '', 'dambewatana', 'dilum@dilum.com', 'anuradhapura', '4578965874', '2020-12-24 00:00:00.000000');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `labs`
--
ALTER TABLE `labs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `phis`
--
ALTER TABLE `phis`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `phi_id` (`phi_id`);

--
-- Indexes for table `pns`
--
ALTER TABLE `pns`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `reports`
--
ALTER TABLE `reports`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `labs`
--
ALTER TABLE `labs`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `phis`
--
ALTER TABLE `phis`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `pns`
--
ALTER TABLE `pns`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `reports`
--
ALTER TABLE `reports`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
