-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 08, 2018 at 08:33 PM
-- Server version: 5.7.23-0ubuntu0.16.04.1
-- PHP Version: 7.0.32-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pharmassistant`
--

-- --------------------------------------------------------

--
-- Table structure for table `expenses`
--

CREATE TABLE `expenses` (
  `expenses_id` int(11) NOT NULL,
  `money` decimal(50,0) DEFAULT NULL,
  `quantity` decimal(50,0) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `item` varchar(50) DEFAULT NULL,
  `vendor` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `expenses`
--

INSERT INTO `expenses` (`expenses_id`, `money`, `quantity`, `date`, `item`, `vendor`) VALUES
(1, '20', '5', '2018-10-27', 'Napa', 'Square'),
(2, '200', '20', '2018-11-05', 'Napa', 'Square'),
(3, '200', '20', '2018-11-06', 'Ace', 'Square');

-- --------------------------------------------------------

--
-- Table structure for table `medicines`
--

CREATE TABLE `medicines` (
  `medicine_id` int(11) NOT NULL,
  `medicine_name` varchar(50) DEFAULT NULL,
  `medicine_type` varchar(50) DEFAULT NULL,
  `company_name` varchar(50) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `quantity` decimal(50,0) DEFAULT NULL,
  `expiry_date` date DEFAULT NULL,
  `shelf` varchar(50) DEFAULT NULL,
  `image_link` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `medicines`
--

INSERT INTO `medicines` (`medicine_id`, `medicine_name`, `medicine_type`, `company_name`, `price`, `quantity`, `expiry_date`, `shelf`, `image_link`) VALUES
(1, 'Napa', 'Paracetamol', 'Square', 5, '40', '2020-01-01', '22C', '/static/Images/napa.jpg'),
(2, 'Ace', 'Paracetamol', 'Beximco', 6, '15', '2020-01-01', '22D', '/static/Images/ace.jpg'),
(3, 'Bandages', 'Utilities', 'Square', 2, '50', '2020-01-01', '12B', '/static/Images/bandages.jpg'),
(5, 'Vicodin', 'Painkiller', 'Vicodin', 20, '7', '2020-01-01', '21D', '/static/Images/vicodin.jpg'),
(6, 'Amoxil', 'Antibiotic', 'Amoxil', 25, '6', '2020-01-01', '20D', '/static/Images/amoxil.jpeg'),
(7, 'Lipitor', 'Blood-Pressure', 'Lipitor', 15, '10', '2020-01-01', '19B', '/static/Images/lipitor.jpg'),
(8, 'Lexapro', 'Anti-Depressant', 'Lexapro', 10, '10', '2020-01-01', '24A', '/static/Images/lexapro.png'),
(9, 'Ambien', 'Sleeping-Pill', 'Ambien', 30, '3', '2020-01-01', '23B', '/static/Images/ambien.jpg'),
(10, 'Coumadin', 'Blood-Thinner', 'Coumadin', 10, '8', '2020-01-01', '24D', '/static/Images/coumadin.jpg'),
(11, 'Flonase', 'Allergies', 'Flonase', 30, '3', '2020-01-01', '20C', '/static/Images/flonase.jpg'),
(12, 'Xanax', 'Anti-Anxiety', 'Xanax', 10, '8', '2020-01-01', '21E', '/static/Images/xanax.jpg'),
(13, 'K-Tab', 'Electrolyte', 'K-Tab', 25, '6', '2020-01-01', '25C', '/static/Images/k-tab.jpg'),
(14, 'Flexeril', 'Muscle-Relaxer', 'Flexeril', 20, '8', '2020-01-01', '23C', '/static/Images/flexeril.jpeg'),
(15, 'Valium', 'Sedative', 'Valium', 30, '5', '2020-01-01', '24B', '/static/Images/valium.jpg'),
(16, 'Mevacor', 'Cholesterol', 'Mevacor', 10, '9', '2020-01-01', '25A', '/static/Images/mevacor.jpg'),
(17, 'Actos', 'Diabetes', 'Actos', 15, '7', '2020-01-01', '23A', '/static/Images/actos.jpg'),
(18, 'Levemir', 'Utilities', 'Levemir', 15, '12', '2020-01-01', '20F', '/static/Images/levemir.jpg'),
(19, 'Diflucan', 'Anti-Fungal', 'Diflucan', 13, '4', '2020-01-01', '18A', '/static/Images/diflucan.jpg'),
(20, 'Catapres', 'Hyper-Tension', 'Catapres', 15, '8', '2020-01-01', '23E', '/static/Images/catapres.jpg'),
(21, 'Ventolin', 'Inhaler', 'Ventolin', 20, '13', '2020-01-01', '23A', '/static/Images/ventolin.jpg'),
(22, 'Advair', 'Inhaler', 'Advair', 25, '13', '2020-01-01', '23A', '/static/Images/advair.jpg'),
(23, 'Plavix', 'Cardiovascular', 'Plavix', 10, '11', '2020-01-01', '23B', '/static/Images/plavix.jpg'),
(24, 'Benadryl', 'Allergies', 'Benadryl', 3.5, '20', '2020-01-01', '22B', '/static/Images/benadryl.jpg'),
(25, 'Pepcid', 'Antacid', 'Pepcid', 10, '11', '2020-01-01', '24F', '/static/Images/pepcid.jpg'),
(26, 'Feosol', 'Antianemics', 'Feosol', 5, '15', '2020-01-01', '21B', '/static/Images/feosol.png'),
(27, 'Synthroid', 'Hormone-Replacement', 'Synthroid', 10, '14', '2020-01-01', '23D', '/static/Images/synthroid.jpg'),
(28, 'ABenadryl', 'Allergies', 'Benadryl', 3.5, '0', '2020-01-01', '22B', '/static/Images/benadryl.jpg'),
(29, 'APepcid', 'Antacid', 'Pepcid', 10, '11', '2020-01-01', '24F', '/static/Images/pepcid.jpg'),
(30, 'AFeosol', 'Antianemics', 'Feosol', 5, '0', '2018-01-01', '21B', '/static/Images/feosol.png'),
(31, 'ASynthroid', 'Hormone-Replacement', 'Synthroid', 10, '14', '2018-01-01', '23D', '/static/Images/synthroid.jpg'),
(32, 'AXylocaine', 'Anesthetic', 'Xylocaine', 10, '15', '2020-01-01', '26A', '/static/Images/xylocaine.jpg'),
(111, 'Nappa', 'Paracetamol', 'Square', 5, '0', '2018-11-27', '22b', '/static/Images/generic.png'),
(1909, 'a', 'paracetamol', 'square', 1, '1', '2018-12-31', 'a', '/static/Images/generic.png'),
(1991, 'a', 'antibiotic', 'square', 1, '1', '2018-12-31', 'a', '/static/Images/generic.png'),
(1992, 'a', 'paracetamol', 'square', 1, '1', '2018-12-31', 'a', '/static/Images/gen2.jpg'),
(1993, 'a', 'paracetamol', 'square', 1, '1', '2018-12-31', 'a', '/static/Images/xylocaine.jpg'),
(4444, 'e', 'e', 'square', 3, '1', '2018-12-31', 'asdad', '/static/Images/generic.png'),
(6464, 'c', 'c', 'square', 1, '1', '2018-12-31', 'c', '/static/Images/generic.png'),
(7474, 'a', 'a', 'square', 1, '1', '2018-01-01', '5454', '/static/Images/generic.png'),
(7575, 'a', 'a', 'square', 1, '1', '2018-01-01', '666', '/static/Images/generic.png'),
(9999, 'a', 'paracetamol', 'square', 1, '1', '2018-12-31', 'a', '/static/Images/generic.png'),
(123131, 'abcbcsdhc', 'paracetamol', 'square', 1, '1', '2018-12-31', 'asdad', '/static/Images/generic.png'),
(1415151, 'a', 'paracetamol', 'square', 1, '1', '2018-12-31', 'a', '/static/Images/generic.png'),
(14151515, 'a', 'paracetamol', 'square', 1, '1', '2018-12-31', 'a', '/static/Images/gen2.jpg'),
(14814814, 'a', 'paracetamol', 'square', 1, '1', '2018-12-31', 'a', '/static/Imagesdiflucan.jpg'),
(15141214, 'a', 'blood-pressure', 'square', 1, '1', '2018-12-31', 'a', '/static/Images/generic.png'),
(15161616, 'a', 'paracetamol', 'square', 1, '1', '2018-12-31', 'a', '/static/Images/gen2.jpg'),
(31913921, 'a', 'paracetamol', 'square', 1, '1', '2018-12-31', 'a', '/static/Images/generic.png'),
(91931931, 'a', 'paracetamol', 'square', 1, '1', '2018-12-31', 'a', '/static/Images/generic.png'),
(123141241, 'a', 'paracetamol', 'square', 1, '1', '2018-12-31', 'a', '/static/Images/generic.png'),
(131312313, 'a', 'paracetamol', 'square', 1, '1', '2018-12-31', 'a', '/static/Images/generic.png'),
(141414141, 'a', 'paracetamol', 'square', 1, '1', '2018-12-31', 'a', '/static/Images/generic.png'),
(1231314213, 'a', 'paracetamol', 'square', 1, '1', '2018-12-31', 'asdadqw', '/static/Images/generic.png'),
(1312313132, 'a', 'paracetamol', 'square', 1, '1', '2018-12-31', 'a', '/static/Images/generic.png'),
(1319319391, 'a', 'paracetamol', 'square', 1, '1', '2018-12-31', 'a', '/static/Images/generic.png'),
(1391931293, 'd', 'paracetamol', 'square', 1, '1', '2018-12-31', 'f', '/static/Images/generic.png');


-- --------------------------------------------------------

--
-- Table structure for table `notifications`
--

CREATE TABLE `notifications` (
  `notificationID` int(11) NOT NULL,
  `type` varchar(50) DEFAULT NULL,
  `notiString` varchar(1000) DEFAULT NULL,
  `medID` varchar(50) DEFAULT NULL,
  `medName` varchar(50) DEFAULT NULL,
  `medShelf` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `notifications`
--

INSERT INTO `notifications` (`notificationID`, `type`, `notiString`, `medID`, `medName`, `medShelf`, `status`) VALUES
(104, 'Empty', 'Vicodin [5, at Shelf: 21D] is out of stock!', '5', 'Vicodin', '21D', 'unread'),
(105, 'Empty', 'Amoxil [6, at Shelf: 20D] is out of stock!', '6', 'Amoxil', '20D', 'unread'),
(106, 'Empty', 'Mevacor [16, at Shelf: 25A] is out of stock!', '16', 'Mevacor', '25A', 'unread'),
(107, 'Empty', 'Actos [17, at Shelf: 23A] is out of stock!', '17', 'Actos', '23A', 'unread'),
(108, 'Expired', 'Diflucan [19, at Shelf: 18A] date expired. Please remove from shelf.', '19', 'Diflucan', '18A', 'unread'),
(109, 'Expired', 'Atova-10 [122, at Shelf: 20-B] date expired. Please remove from shelf.', '122', 'Atova-10', '20-B', 'unread');
-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `id` int(11) NOT NULL,
  `order_id` varchar(50) DEFAULT NULL,
  `vendor_id` int(11) DEFAULT NULL,
  `company_name` varchar(50) DEFAULT NULL,
  `medicine` varchar(50) DEFAULT NULL,
  `quantity` decimal(50,0) DEFAULT NULL,
  `due_date` date DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `cost` decimal(50,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`id`, `order_id`, `vendor_id`, `company_name`, `medicine`, `quantity`, `due_date`, `status`, `cost`) VALUES
(1, '3', 2, 'Beximco', 'Ace', '11', '2018-11-08', 'false', '53');

-- --------------------------------------------------------

--
-- Table structure for table `ordersList`
--

CREATE TABLE `ordersList` (
  `order_id` int(11) NOT NULL,
  `company_name` varchar(50) DEFAULT NULL,
  `total_cost` float DEFAULT NULL,
  `paid_amount` float DEFAULT NULL,
  `due_amount` float DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `order_date` date DEFAULT NULL,
  `due_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ordersList`
--

INSERT INTO `ordersList` (`order_id`, `company_name`, `total_cost`, `paid_amount`, `due_amount`, `status`, `order_date`, `due_date`) VALUES
(1, 'Square', 48, 48, 0, 'false', '2018-11-08', '2018-11-08'),
(2, 'Square', 48, 48, 0, 'false', '2018-11-08', '2018-11-08'),
(3, 'Beximco', 52.8, 52.8, 0, 'false', '2018-11-08', '2018-11-08');

-- --------------------------------------------------------

--
-- Table structure for table `sellings`
--

CREATE TABLE `sellings` (
  `sellings_id` int(11) NOT NULL,
  `money` decimal(50,0) DEFAULT NULL,
  `quantity` decimal(50,0) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `item` varchar(50) DEFAULT NULL,
  `customer_name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sellings`
--

INSERT INTO `sellings` (`sellings_id`, `money`, `quantity`, `date`, `item`, `customer_name`) VALUES
(1, '25', '5', '2018-10-27', 'Napa', 'John');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `full_name` varchar(50) DEFAULT NULL,
  `user_type` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `full_name`, `user_type`) VALUES
(1, 'a', 'a', 'a', 'admin'),
(2, 'b', 'b', 'b', 'normal'),
(3, 'John', 'pass', 'John Smith', 'admin'),
(4, 'Sarah', 'pass', 'Sarah Jane', 'normal'),
(5, 'James', 'james', 'J. Jonah Jameson', 'normal');

-- --------------------------------------------------------

--
-- Table structure for table `vendors`
--

CREATE TABLE `vendors` (
  `vendor_id` int(11) NOT NULL,
  `company_name` varchar(50) DEFAULT NULL,
  `contact_number` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vendors`
--

INSERT INTO `vendors` (`vendor_id`, `company_name`, `contact_number`) VALUES
(1, 'Square', '01111111111'),
(2, 'Beximco', '01111111111'),
(3, 'Amoxil', '01111111111');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `expenses`
--
ALTER TABLE `expenses`
  ADD PRIMARY KEY (`expenses_id`);

--
-- Indexes for table `medicines`
--
ALTER TABLE `medicines`
  ADD PRIMARY KEY (`medicine_id`);

--
-- Indexes for table `notifications`
--
ALTER TABLE `notifications`
  ADD PRIMARY KEY (`notificationID`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ordersList`
--
ALTER TABLE `ordersList`
  ADD PRIMARY KEY (`order_id`);

--
-- Indexes for table `sellings`
--
ALTER TABLE `sellings`
  ADD PRIMARY KEY (`sellings_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `vendors`
--
ALTER TABLE `vendors`
  ADD PRIMARY KEY (`vendor_id`),
  ADD UNIQUE KEY `company_name` (`company_name`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `expenses`
--
ALTER TABLE `expenses`
  MODIFY `expenses_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `medicines`
--
ALTER TABLE `medicines`
  MODIFY `medicine_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1391931294;
--
-- AUTO_INCREMENT for table `notifications`
--
ALTER TABLE `notifications`
  MODIFY `notificationID` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `ordersList`
--
ALTER TABLE `ordersList`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `sellings`
--
ALTER TABLE `sellings`
  MODIFY `sellings_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `vendors`
--
ALTER TABLE `vendors`
  MODIFY `vendor_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
