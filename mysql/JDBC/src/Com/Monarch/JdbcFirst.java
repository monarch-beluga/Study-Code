package Com.Monarch;

import java.sql.*;

// 第一个JDBC程序
public class JdbcFirst {
    public static void main(String[] args) throws ClassNotFoundException, SQLException {
        // 1. 加载驱动
        Class.forName("com.mysql.cj.jdbc.Driver");         // 固定写法，加载驱动

        // 2. 用户信息和url
        String url = "jdbc:mysql://localhost:3306/jdbcStudy?userUnicode=true&characterEncoding=utf8&useSSL=true";
        String username = "root";
        String password = "123456";

        // 3. 连接成功，获取数据库对象
        Connection connection = DriverManager.getConnection(url, username, password);

        // 4. 获取执行sql的对象
        Statement statement = connection.createStatement();

        // 5. 执行sql的对象去执行sql，可能存在结果，查看返回结果
        // statement.executeQuery("use jdbcStudy;");        // 使用指定数据库

        String sql = "select * from users";
        ResultSet resultSet = statement.executeQuery(sql);  // 返回结果集,结果集中封装了我们全部的查询出来的结果

        System.out.println("id\tname\tpassword\temail\tbirthday");
        while (resultSet.next()){
            System.out.print(resultSet.getObject("id")+"\t");
            System.out.print(resultSet.getObject("name")+"\t");
            System.out.print(resultSet.getObject("password")+"\t");
            System.out.print(resultSet.getObject("email")+"\t");
            System.out.println(resultSet.getObject("birthday"));
        }

        // 6. 释放连接
        resultSet.close();
        statement.close();
        connection.close();
    }
}
