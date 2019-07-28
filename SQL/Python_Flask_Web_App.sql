SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Database: `Python-Flask-Web-App`
-- Create if it doesn't exist
--
CREATE DATABASE IF NOT EXISTS Python_Flask_Web_App;

--
-- Specify we're using the above created database.
--
USE Python_Flask_Web_App;

DELIMITER $$

--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser` (IN `p_forename` VARCHAR(20), IN `p_surname` VARCHAR(20), IN `p_email` VARCHAR(50), IN `p_password` VARCHAR(500))  BEGIN
    if (select exists (select 1 from customer where EmailAddress = p_email)) THEN
        select 'User already exists';
    ELSE
     
        insert into customer 
        (
            User_ID,
            User_Forname,
            User_Surname,
            EmailAddress,
            Password
        )
        values
        (
            NULL,
            p_forename,
            p_surname,
            p_email ,
            p_password
        );
     
    END IF;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `User_ID` int(11) NOT NULL,
  `User_Forname` varchar(30) NOT NULL,
  `User_Surname` varchar(30) NOT NULL,
  `EmailAddress` varchar(50) NOT NULL,
  `Password` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer`
--

--
-- This user password is default01!!
-- Can be changed in the Account section of the site once logged in.
--
INSERT INTO `customer` (`User_ID`, `User_Forname`, `User_Surname`, `EmailAddress`, `Password`) VALUES
(0, 'Exampe', 'Customer', 'Exampleustomer01@icloud.com', '$2b$12$qBCR00jqcIyV0Nbs4hynBuTOB6t59rEMMORNb739SfEVuyjG4y4AW');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `Order_ID` int(11) NOT NULL,
  `Order_Total` decimal(10,2) NOT NULL,
  `Order_Timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `Order_Complete` char(1) NOT NULL,
  `Table_No` int(2) NOT NULL,
  `fk1_User_ID` int(11) NOT NULL,
  `fk2_Staff_ID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


-- --------------------------------------------------------

--
-- Table structure for table `order_items`
--

CREATE TABLE `order_items` (
  `Order_Items_ID` int(11) NOT NULL,
  `Quantity` int(11) NOT NULL,
  `fk1_Product_ID` int(11) NOT NULL,
  `fk2_Order_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `Product_ID` int(11) NOT NULL,
  `Product_Name` varchar(30) NOT NULL,
  `Product_Cat` varchar(20) NOT NULL,
  `Price` decimal(6,2) NOT NULL,
  `Product_Image` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`Product_ID`, `Product_Name`, `Product_Cat`, `Price`, `Product_Image`) VALUES
(1, 'Caffe Latte', 'Coffee_Latte', '2.50', 'Latte1-min.jpg'),
(2, 'Flat White', 'Coffee_Latte', '2.50', 'Latte2-min.jpg'),
(3, 'Caffe Mocha', 'Coffee_Mocha', '2.60', 'Mocha1-min.jpg'),
(4, 'White Chocolate Mocha', 'Coffee_Mocha', '2.60', 'Mocha2-min.jpg'),
(5, 'Latte Macchiato', 'Coffee_Macchiato', '2.40', 'Macchiato1-min.jpg'),
(6, 'Caramel Macchiato', 'Coffee_Macchiato', '2.40', 'Macchiato2-min.jpg'),
(7, 'Cappuccino', 'Coffee_Cappuccino', '2.10', 'Cappucino1-min.jpg'),
(8, 'Caffe Americano', 'Coffee_Americano', '1.90', 'Americano1-min.jpg'),
(9, 'Cortado', 'Coffee_Espresso', '2.30', 'Espresso1-min.jpg'),
(10, 'Espresso', 'Coffee_Espresso', '2.30', 'Espresso2-min.jpg'),
(11, 'Espresso Macchiato', 'Coffee_Espresso', '2.30', 'Espresso3-min.jpg'),
(12, 'Banana Bread', 'Bakery', '1.20', 'Bakery1-min.jpg'),
(13, 'Blueberry Muffin', 'Bakery', '1.00', 'Bakery2-min.jpg'),
(14, 'Caramel Shortbread', 'Bakery', '0.90', 'Bakery3-min.jpg'),
(15, 'Carrot Cake', 'Bakery', '1.20', 'Bakery4-min.jpg'),
(16, 'Lemon Loaf', 'Bakery', '0.90', 'Bakery6-min.jpg'),
(17, 'Triple Choc Muffin', 'Bakery', '0.70', 'Bakery7-min.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `Staff_ID` int(11) NOT NULL,
  `Email_Address` varchar(30) NOT NULL,
  `Password` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `staff`
--

--
-- This staff password is default01!!
-- Can be changed in the Account section of the site once logged in.
--
INSERT INTO `staff` (`Staff_ID`, `Email_Address`, `Password`) VALUES
(0, 'admin@coffeeshack.org', '$2b$12$qBCR00jqcIyV0Nbs4hynBuTOB6t59rEMMORNb739SfEVuyjG4y4AW');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD UNIQUE KEY `User_ID` (`User_ID`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD UNIQUE KEY `Order_ID` (`Order_ID`);

--
-- Indexes for table `order_items`
--
ALTER TABLE `order_items`
  ADD UNIQUE KEY `Order_Items_ID` (`Order_Items_ID`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD UNIQUE KEY `Product_ID` (`Product_ID`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD UNIQUE KEY `Staff_ID` (`Staff_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `User_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `Order_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- AUTO_INCREMENT for table `order_items`
--
ALTER TABLE `order_items`
  MODIFY `Order_Items_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
