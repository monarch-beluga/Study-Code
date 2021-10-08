package Com.Monarch.StatementTest;

import Com.Monarch.utils.JdbcUtils;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class TestSelect {
    public static void main(String[] args) throws SQLException {
        Connection conn = JdbcUtils.getConnection();    // 获取连接
        Statement st = conn.createStatement();          // 获取SQL的执行对象

        String sql = "select * from users where id = 1";
        ResultSet rs = st.executeQuery(sql);
        while (rs.next()){
            System.out.println(rs.getString("name"));
        }

        JdbcUtils.release(conn, st, rs);                    // 释放资源
    }
}
