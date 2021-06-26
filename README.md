# Test

## Build Setup

```bash
# install dependencies
$ npm install

# serve with hot reload at localhost:3000
$ npm run dev

# build for production and launch server
$ npm run build
$ npm run start

# generate static project
$ npm run generate
```

For detailed explanation on how things work, check out [Nuxt.js docs](https://nuxtjs.org).

# 需要開的資料表

* 商品資料表
* 訂單資料表
* 會員資料表

## 商品資料表 - Product
* ID
* Name
* Price
* Description

## 訂單主檔資料表 - Order
* ID
* MemberID
* Description

## 訂單明細檔 - OrderItem
* ID
* OrderID
* ProductID
* Quantity

## 會員資料表 - Member
* ID
* FirstName
* LastName
* Address
* Level
