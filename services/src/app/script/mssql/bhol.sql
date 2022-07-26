USE [master]
GO
/****** Object:  Database [BHOL]    Script Date: 6/30/2022 9:40:05 PM ******/
CREATE DATABASE [BHOL]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'BHOL', FILENAME = N'/Users/daotnguyen/Mssql/Data/BHOL.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'BHOL_log', FILENAME = N'/Users/daotnguyen/Mssql/Data/BHOL_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
GO
ALTER DATABASE [BHOL] SET COMPATIBILITY_LEVEL = 130
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [BHOL].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [BHOL] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [BHOL] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [BHOL] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [BHOL] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [BHOL] SET ARITHABORT OFF 
GO
ALTER DATABASE [BHOL] SET AUTO_CLOSE ON 
GO
ALTER DATABASE [BHOL] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [BHOL] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [BHOL] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [BHOL] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [BHOL] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [BHOL] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [BHOL] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [BHOL] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [BHOL] SET  ENABLE_BROKER 
GO
ALTER DATABASE [BHOL] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [BHOL] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [BHOL] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [BHOL] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [BHOL] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [BHOL] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [BHOL] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [BHOL] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [BHOL] SET  MULTI_USER 
GO
ALTER DATABASE [BHOL] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [BHOL] SET DB_CHAINING OFF 
GO
ALTER DATABASE [BHOL] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [BHOL] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [BHOL] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [BHOL] SET QUERY_STORE = OFF
GO
USE [BHOL]
GO
ALTER DATABASE SCOPED CONFIGURATION SET LEGACY_CARDINALITY_ESTIMATION = OFF;
GO
ALTER DATABASE SCOPED CONFIGURATION SET MAXDOP = 0;
GO
ALTER DATABASE SCOPED CONFIGURATION SET PARAMETER_SNIFFING = ON;
GO
ALTER DATABASE SCOPED CONFIGURATION SET QUERY_OPTIMIZER_HOTFIXES = OFF;
GO
USE [BHOL]
GO
/****** Object:  Table [dbo].[BankAccount]    Script Date: 6/30/2022 9:40:05 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[BankAccount](
	[id_bank_account] [varchar](36) NOT NULL,
	[id_driver] [varchar](36) NOT NULL,
	[account_no] [varchar](50) NULL,
	[account_name] [nvarchar](256) NULL,
	[bank_name] [nvarchar](50) NULL,
	[bank_branch] [nvarchar](50) NULL,
PRIMARY KEY CLUSTERED 
(
	[id_bank_account] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Branch]    Script Date: 6/30/2022 9:40:05 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Branch](
	[id_branch] [varchar](36) NOT NULL,
	[id_partner] [varchar](36) NOT NULL,
	[name_branch] [nvarchar](100) NULL,
	[created_date] [datetime2] NULL,
	[created_by] [varchar](36) NULL,
	[modified_date] [datetime2] NULL,
	[modified_by] [varchar](36) NULL,
	[status] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[id_branch] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Contract]    Script Date: 6/30/2022 9:40:05 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Contract](
	[id_contract] [varchar](36) NOT NULL,
	[id_employee] [varchar](36) NOT NULL,
	[id_partner] [varchar](36) NOT NULL,
	[representation] [nvarchar](100) NULL,
	[tax_code_partner] [varchar](50) NULL,
	[number_of_registered_branch] [int] NULL,
	[effective_time] [datetime2] NULL,
	[commission_percentage] [float] NULL,
	[activation_fee] [float] NULL,
	[status] [int] NULL,
	[created_date] [datetime2] NULL,
	[created_by] [varchar](36) NULL,
PRIMARY KEY CLUSTERED 
(
	[id_contract] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[City]    Script Date: 6/30/2022 9:40:05 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[City](
	[id_city] [varchar](36) NOT NULL,
	[city_name] [nvarchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id_city] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[District]    Script Date: 6/30/2022 9:40:05 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[District](
	[id_district] [varchar](36) NOT NULL,
	[district_name] [nvarchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id_district] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[DeliveryAddress]    Script Date: 6/30/2022 9:40:05 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[DeliveryAddress](
	[id_delivery_address] [varchar](36) NOT NULL,
	[id_user] [varchar](36) NOT NULL,
	[city] [nvarchar](50) NULL,
	[district] [nvarchar](50) NULL,
	[detail] [nvarchar](256) NULL,
PRIMARY KEY CLUSTERED 
(
	[id_delivery_address] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[HomeAddress]    Script Date: 6/30/2022 9:40:05 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[HomeAddress](
	[id_user] [varchar](36) NOT NULL,
	[city] [nvarchar](50) NOT NULL,
	[district] [nvarchar](50) NOT NULL,
	[detail] [nvarchar](256) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id_user] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[BranchAddress]    Script Date: 6/30/2022 9:40:05 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[BranchAddress](
	[id_branch] [varchar](36) NOT NULL,
	[city] [nvarchar](50) NOT NULL,
	[district] [nvarchar](50) NOT NULL,
	[detail] [nvarchar](256) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id_branch] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Driver]    Script Date: 6/30/2022 9:40:05 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Driver](
	[id_driver] [varchar](36) NOT NULL,
	[id_bank_account] [varchar](36) DEFAULT NULL,
	[id_card] [varchar](50) NOT NULL,
	[license_plates] [varchar](50) NULL,
	[working_city] [nvarchar](50) NOT NULL,
	[working_district] [nvarchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id_driver] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Order]    Script Date: 6/30/2022 9:40:05 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Order](
	[id_order] [varchar](36) NOT NULL,
	[id_partner] [varchar](36) NOT NULL,
	[id_pay] [varchar](36) NOT NULL,
	[id_buyer] [varchar](36) NOT NULL,
	[id_driver] [varchar](36) NOT NULL,
	[id_delivery_address] [varchar](36) NOT NULL,
	[status_order] [int] NULL,
	[cost_order] [float] NULL,
	[cost_transport] [float] NULL,
	[sumcost] [float] NULL,
	[is_handler] [bit] NULL,
	[created_date] [datetime2] NULL,
	[modified_date] [datetime2] NULL,
PRIMARY KEY CLUSTERED
(
	[id_order] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[OrderDetail]    Script Date: 6/30/2022 9:40:05 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[OrderDetail](
	[id_order_detail] [varchar](36) NOT NULL,
	[id_order] [varchar](36) NOT NULL,
	[id_product] [varchar](36) NOT NULL,
	[quantity] [int] NULL,
	[price] [float] NULL,
PRIMARY KEY CLUSTERED 
(
	[id_order_detail] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Partner]    Script Date: 6/30/2022 9:40:05 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Partner](
	[id_partner] [varchar](36) NOT NULL,
	[representation] [nvarchar](100) NULL,
	[number_of_branch] [int] NULL,
	[number_order_of_day] [int] NULL,
	[product_shipping] [ntext] NULL,
	[tax_code] [varchar](50) NULL,
PRIMARY KEY CLUSTERED 
(
	[id_partner] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Pay]    Script Date: 6/30/2022 9:40:05 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Pay](
	[id_pay] [varchar](36) NOT NULL,
	[name_pay] [nvarchar](100) NULL,
PRIMARY KEY CLUSTERED 
(
	[id_pay] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Product]    Script Date: 6/30/2022 9:40:05 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Product](
	[id_product] [varchar](36) NOT NULL,
	[id_branch] [varchar](36) NOT NULL,
	[id_partner] [varchar](36) NOT NULL,
	[id_category] [varchar](36) NOT NULL,
	[name_product] [nvarchar](100) NULL,
	[describe] [ntext] NULL,
	[quantity] [int] NOT NULL,
	[price] [float] NOT NULL,
	[created_date] [datetime2] NULL,
	[created_by] [varchar](36) NULL,
	[modified_date] [datetime2] NULL,
	[modified_by] [varchar](36) NULL,
	[status] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[id_product] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Category]    Script Date: 6/30/2022 9:40:05 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Category](
	[id_category] [varchar](36) NOT NULL,
	[name_category] [nvarchar](100) NULL,
PRIMARY KEY CLUSTERED 
(
	[id_category] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Role]    Script Date: 6/30/2022 9:40:05 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Role](
	[id_role] [varchar](36) NOT NULL,
	[name_role] [nvarchar](100) NULL,
	[can_edit_data] [bit] NULL,
	[can_edit_user] [bit] NULL,
	[can_manage_ui] [bit] NULL,
PRIMARY KEY CLUSTERED 
(
	[id_role] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[User]    Script Date: 6/30/2022 9:40:05 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[User](
	[id_user] [varchar](36) NOT NULL,
	[name] [varchar](100) NOT NULL,
	[username] [varchar](100) NOT NULL,
	[password] [varchar](36) NOT NULL,
	[phone_number] [varchar](18) NOT NULL,
	[dob] [date] NULL,
	[email] [varchar](100) NULL,
	[created_date] [datetime2] NULL,
	[created_by] [varchar](36) NULL,
	[modified_date] [datetime2] NULL,
	[modified_by] [varchar](36) NULL,
    [role] [int] NOT NULL DEFAULT 0,
	[status] [int] NULL
PRIMARY KEY CLUSTERED 
(
	[id_user] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[BankAccount]  WITH CHECK ADD  CONSTRAINT [Fk_BranchAccount_Driver] FOREIGN KEY([id_driver])
REFERENCES [dbo].[Driver] ([id_driver])
GO
ALTER TABLE [dbo].[BankAccount] CHECK CONSTRAINT [Fk_BranchAccount_Driver]
GO
ALTER TABLE [dbo].[Branch]  WITH CHECK ADD  CONSTRAINT [Fk_Branch_Partner] FOREIGN KEY([id_partner])
REFERENCES [dbo].[Partner] ([id_partner])
GO
ALTER TABLE [dbo].[Branch] CHECK CONSTRAINT [Fk_Branch_Partner]
GO
ALTER TABLE [dbo].[Contract]  WITH CHECK ADD  CONSTRAINT [Fk_Contract_Employee] FOREIGN KEY([id_employee])
REFERENCES [dbo].[User] ([id_user])
GO
ALTER TABLE [dbo].[Contract] CHECK CONSTRAINT [Fk_Contract_Employee]
GO
ALTER TABLE [dbo].[Contract]  WITH CHECK ADD  CONSTRAINT [Fk_Contract_Partner] FOREIGN KEY([id_partner])
REFERENCES [dbo].[Partner] ([id_partner])
GO
ALTER TABLE [dbo].[Contract] CHECK CONSTRAINT [Fk_Contract_Partner]
GO
ALTER TABLE [dbo].[DeliveryAddress]  WITH CHECK ADD  CONSTRAINT [Fk_DeliveryAddress_User] FOREIGN KEY([id_user])
REFERENCES [dbo].[User] ([id_user])
GO
ALTER TABLE [dbo].[DeliveryAddress] CHECK CONSTRAINT [Fk_DeliveryAddress_User]
GO
ALTER TABLE [dbo].[HomeAddress]  WITH CHECK ADD  CONSTRAINT [Fk_HomeAddress_User] FOREIGN KEY([id_user])
REFERENCES [dbo].[User] ([id_user])
GO
ALTER TABLE [dbo].[HomeAddress] CHECK CONSTRAINT [Fk_HomeAddress_User]
GO
ALTER TABLE [dbo].[BranchAddress]  WITH CHECK ADD  CONSTRAINT [Fk_BranchAddress_Branch] FOREIGN KEY([id_branch])
REFERENCES [dbo].[Branch] ([id_branch])
GO
ALTER TABLE [dbo].[BranchAddress] CHECK CONSTRAINT [Fk_BranchAddress_Branch]
GO
ALTER TABLE [dbo].[Order]  WITH CHECK ADD  CONSTRAINT [Fk_Order_DeliveryAddress] FOREIGN KEY([id_delivery_address])
REFERENCES [dbo].[DeliveryAddress] ([id_delivery_address])
GO
ALTER TABLE [dbo].[Order] CHECK CONSTRAINT [Fk_Order_DeliveryAddress]
GO
ALTER TABLE [dbo].[Order]  WITH CHECK ADD  CONSTRAINT [Fk_Order_Partner] FOREIGN KEY([id_partner])
REFERENCES [dbo].[Partner] ([id_partner])
GO
ALTER TABLE [dbo].[Order] CHECK CONSTRAINT [Fk_Order_Partner]
GO
ALTER TABLE [dbo].[Order]  WITH CHECK ADD  CONSTRAINT [Fk_Order_Pay] FOREIGN KEY([id_pay])
REFERENCES [dbo].[Pay] ([id_pay])
GO
ALTER TABLE [dbo].[Order] CHECK CONSTRAINT [Fk_Order_Pay]
GO
ALTER TABLE [dbo].[Order]  WITH CHECK ADD  CONSTRAINT [Fk_Order_User] FOREIGN KEY([id_buyer])
REFERENCES [dbo].[User] ([id_user])
GO
ALTER TABLE [dbo].[Order] CHECK CONSTRAINT [Fk_Order_User]
GO
ALTER TABLE [dbo].[Order]  WITH CHECK ADD  CONSTRAINT [Fk_Order_Driver] FOREIGN KEY([id_driver])
REFERENCES [dbo].[Driver] ([id_driver])
GO
ALTER TABLE [dbo].[Order] CHECK CONSTRAINT [Fk_Order_Driver]
GO
ALTER TABLE [dbo].[OrderDetail]  WITH CHECK ADD  CONSTRAINT [Fk_OrderDetail_Order] FOREIGN KEY([id_order])
REFERENCES [dbo].[Order] ([id_order])
GO
ALTER TABLE [dbo].[OrderDetail] CHECK CONSTRAINT [Fk_OrderDetail_Order]
GO
ALTER TABLE [dbo].[OrderDetail]  WITH CHECK ADD  CONSTRAINT [Fk_OrderDetail_Product] FOREIGN KEY([id_product])
REFERENCES [dbo].[Product] ([id_product])
GO
ALTER TABLE [dbo].[OrderDetail] CHECK CONSTRAINT [Fk_OrderDetail_Product]
GO
ALTER TABLE [dbo].[Product]  WITH CHECK ADD  CONSTRAINT [Fk_Product_Branch] FOREIGN KEY([id_branch])
REFERENCES [dbo].[Branch] ([id_branch])
GO
ALTER TABLE [dbo].[Product] CHECK CONSTRAINT [Fk_Product_Branch]
GO
ALTER TABLE [dbo].[Product]  WITH CHECK ADD  CONSTRAINT [Fk_Product_Partner] FOREIGN KEY([id_partner])
REFERENCES [dbo].[Partner] ([id_partner])
GO
ALTER TABLE [dbo].[Product] CHECK CONSTRAINT [Fk_Product_Partner]
GO
ALTER TABLE [dbo].[Product]  WITH CHECK ADD  CONSTRAINT [Fk_Product_Category] FOREIGN KEY([id_category])
REFERENCES [dbo].[Category] ([id_category])
GO
ALTER TABLE [dbo].[Product] CHECK CONSTRAINT [Fk_Product_Category]
GO
ALTER TABLE [dbo].[Driver]  WITH CHECK ADD  CONSTRAINT [Fk_Driver_User] FOREIGN KEY([id_driver])
REFERENCES [dbo].[User] ([id_user])
GO
ALTER TABLE [dbo].[Driver] CHECK CONSTRAINT [Fk_Driver_User]
GO
ALTER TABLE [dbo].[Driver]  WITH CHECK ADD  CONSTRAINT [Fk_Driver_BankAccount] FOREIGN KEY([id_bank_account])
REFERENCES [dbo].[BankAccount] ([id_bank_account])
GO
ALTER TABLE [dbo].[Driver] CHECK CONSTRAINT [Fk_Driver_BankAccount]
GO
ALTER TABLE [dbo].[Partner]  WITH CHECK ADD  CONSTRAINT [Fk_Partner_User] FOREIGN KEY([id_partner])
REFERENCES [dbo].[User] ([id_user])
GO
ALTER TABLE [dbo].[Partner] CHECK CONSTRAINT [Fk_Partner_User]
GO
USE [master]
GO
ALTER DATABASE [BHOL] SET  READ_WRITE 
GO


-- USE [BHOL]
-- GO
-- INSERT INTO [Role] (id_role, name_role, can_edit_data, can_edit_user, can_manage_ui)
-- VALUES(db_owner, db_owner)
