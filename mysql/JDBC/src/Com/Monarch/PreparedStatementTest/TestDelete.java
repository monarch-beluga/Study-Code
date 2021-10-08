package Com.Monarch.PreparedStatementTest;

import Com.Monarch.utils.JdbcUtils;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.text.MessageFormat;
import java.text.ParseException;

public class TestDelete {
    public static void main(String[] args) throws SQLException, ParseException {
        Connection conn = JdbcUtils.getConnection();
        String sql = "delete from users where id=?";
        PreparedStatement pst = conn.prepareStatement(sql);            // 预编译SQL

        pst.setInt(1, 4);

        int i = pst.executeUpdate();
        if (i > 0)
            System.out.println(MessageFormat.format("删除{0}条数据", i));
        JdbcUtils.release(conn, pst);                    // 释放资源
    }
}
