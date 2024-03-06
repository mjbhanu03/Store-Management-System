-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 06, 2024 at 05:21 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `stockmanagement`
--

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `c_id` int(11) NOT NULL,
  `name` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`c_id`, `name`) VALUES
(1, 'Mobile'),
(3, 'Accessorie');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `contact` bigint(10) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `dob` date NOT NULL,
  `doj` date NOT NULL,
  `email` varchar(70) NOT NULL,
  `password` varchar(15) NOT NULL,
  `utype` varchar(10) NOT NULL,
  `address` varchar(200) NOT NULL,
  `salary` bigint(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`id`, `name`, `contact`, `gender`, `dob`, `doj`, `email`, `password`, `utype`, `address`, `salary`) VALUES
(1, 'Mange Jay', 7016515225, 'Male', '2003-02-27', '2024-02-17', 'jaymange263@gmail.co', '12ka4', 'Admin', 'Hirji MIstri Road\nJamnagar	- 361005	', 200000000),
(2, 'JG', 5445025565, 'Male', '2024-05-23', '2024-02-12', 'jg#gmail.com', '256', 'Admin', 'Dsas', 10000000),
(3, 'Bhavya ', 51542050331, 'Male', '2024-02-28', '2024-02-27', 'vkshah20178', '123', 'Admin', 'Dwdwd', 123),
(4, 'Neha ', 7203085698, 'Female', '2024-02-06', '2024-02-28', 'nehamange99@gmail.co', '123', 'Admin', 'Jamnagar', 180000),
(5, 'Avi', 7894561232, 'Male', '2003-02-06', '2024-02-29', 'avinashshiyani760@gm', '123', 'Employee', 'Jamnagar', 10000),
(6, 'kalpana', 7894561230, 'Female', '2024-03-07', '2024-03-14', 'avinashshiyani760@gmail.com\r\n', '123', 'Admin', 'Jamnagar', 18000),
(7, 'Bhavya Sha', 7894613200, 'Male', '2003-05-05', '2024-03-04', 'bhavya@gmail.com', '123', 'Employee', 'Jamnagar', 10000);

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `id` int(11) NOT NULL,
  `category` varchar(10) NOT NULL,
  `supplier` varchar(10) NOT NULL,
  `name` varchar(10) NOT NULL,
  `price` int(10) NOT NULL,
  `quantity` int(10) NOT NULL,
  `status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`id`, `category`, `supplier`, `name`, `price`, `quantity`, `status`) VALUES
(1, 'Accessorie', 'Apporva', 'iPhone 14 ', 890000, 5, 'Active'),
(2, 'Mobile', 'Mange Jay', 'iPhone 14 ', 86000, 1, 'Active'),
(4, 'Mobile', 'Avi Shiyan', 'Laptop Ins', 85000, 1, 'Active'),
(5, 'Mobile', 'Mange Jay', 'iPhone 13', 52000, 6, 'Active'),
(6, 'Accessorie', 'Preet Jogi', 'Longines W', 1350, 96, 'Active'),
(7, 'Mobile', 'Avi Shiyan', 'iPhone 12 ', 49000, 5, 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `supplier`
--

CREATE TABLE `supplier` (
  `invoice_no` int(10) NOT NULL,
  `name` varchar(20) NOT NULL,
  `description` varchar(100) NOT NULL,
  `contact` bigint(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `supplier`
--

INSERT INTO `supplier` (`invoice_no`, `name`, `description`, `contact`) VALUES
(101, 'Mange Jay', 'MJ\'s CLUB\nJamnagar', 7016515225),
(102, 'Avi Shiyani', 'Anjani Courier\nJamnagar\n', 7203082056),
(103, 'Apporva', 'AS Tuitions - Rajkot\n', 89564578),
(111, 'Maggie ', 'Maggie CAfe - Mumbai', 7894561230),
(112, 'Preet Jogia', 'Ganesh Watchs - Jamnagar', 8947563210),
(118, 'Hamid Raza', 'Grocery Store Bhanvad', 79461385256);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`c_id`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `c_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
