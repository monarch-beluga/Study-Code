package Com.Monarch.PreparedStatementTest;

import Com.Monarch.utils.JdbcUtils;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.text.MessageFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class TestInsert {
    public static void main(String[] args) throws SQLException, ParseException {
        Connection conn = JdbcUtils.getConnection();
        String sql = "insert into users(id, name, password, email, birthday)" +
                " VALUES (?, ?, ?, ?, ?)";                  // 问号为占位符
        PreparedStatement pst = conn.prepareStatement(sql);            // 预编译SQL

        // 手动给参数赋值
        pst.setInt(1, 4);
        pst.setString(2, "zhangsan");
        pst.setString(3, "123");
        pst.setString(4, "21548724@qq.com");
        // 注意点：java.util里的Date与sql中的有区别
        // new java.sql.Date(new java.util.Date().getTime())
        // 先用java.util.Date().getTime()获得时间戳，然后再转化为sql中的Date
        Date date = new SimpleDateFormat("yyyy-MM-dd").parse("2020-01-02");
        pst.setDate(5, new java.sql.Date(date.getTime()));

        int i = pst.executeUpdate();
        if (i > 0)
            System.out.println(MessageFormat.format("插入{0}条数据", i));
        JdbcUtils.release(conn, pst);                    // 释放资源
    }
}
