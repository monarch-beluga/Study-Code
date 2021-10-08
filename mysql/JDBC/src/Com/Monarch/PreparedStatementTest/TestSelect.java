package Com.Monarch.PreparedStatementTest;

import Com.Monarch.utils.JdbcUtils;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.text.ParseException;

public class TestSelect {
    public static void main(String[] args) throws SQLException, ParseException {
        Connection conn = JdbcUtils.getConnection();
        String sql = "select *  from users where id=?";
        PreparedStatement pst = conn.prepareStatement(sql);            // 预编译SQL

        pst.setInt(1, 1);

        ResultSet rs = pst.executeQuery();
        while (rs.next()){
            System.out.println(rs.getString("name"));
        }
        JdbcUtils.release(conn, pst, rs);                    // 释放资源
    }
}
