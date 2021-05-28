package Com.Monarch.StatementTest;

import Com.Monarch.utils.JdbcUtils;

import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Statement;
import java.text.MessageFormat;

public class TestDelete {
    public static void main(String[] args) throws SQLException {
        Connection conn = JdbcUtils.getConnection();    // 获取连接
        Statement st = conn.createStatement();          // 获取SQL的执行对象
        String sql = "delete from users where id=4";
        int i = st.executeUpdate(sql);
        if (i > 0)
            System.out.println(MessageFormat.format("删除{0}条数据", i));
        JdbcUtils.release(conn, st);                    // 释放资源
    }
}
