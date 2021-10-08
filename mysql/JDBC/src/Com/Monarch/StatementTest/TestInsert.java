package Com.Monarch.StatementTest;

import Com.Monarch.utils.JdbcUtils;

import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Statement;
import java.text.MessageFormat;

public class TestInsert {
    public static void main(String[] args) throws SQLException {
        Connection conn = JdbcUtils.getConnection();    // 获取连接
        Statement st = conn.createStatement();          // 获取SQL的执行对象
        String sql = "insert into users(id, name, password, email, birthday)" +
                " VALUES (4, 'monarch', '123456', '32165487@qq.com', '2021-01-01')";
        int i = st.executeUpdate(sql);
        if (i > 0)
            System.out.println(MessageFormat.format("插入{0}条数据", i));
        JdbcUtils.release(conn, st);                    // 释放资源
    }
}
