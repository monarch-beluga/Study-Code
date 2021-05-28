package Com.Monarch.PreparedStatementTest;

import Com.Monarch.utils.JdbcUtils;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.text.MessageFormat;
import java.text.ParseException;

public class TestUpdate {
    public static void main(String[] args) throws SQLException, ParseException {
        Connection conn = JdbcUtils.getConnection();
        String sql = "update users set name = ? where id=?";
        PreparedStatement pst = conn.prepareStatement(sql);            // 预编译SQL

        pst.setString(1, "白鲸");
        pst.setInt(2, 1);

        int i = pst.executeUpdate();
        if (i > 0)
            System.out.println(MessageFormat.format("更新{0}条数据", i));
        JdbcUtils.release(conn, pst);                    // 释放资源
    }
}
