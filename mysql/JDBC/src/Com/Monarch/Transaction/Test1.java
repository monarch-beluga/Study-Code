package Com.Monarch.Transaction;

import Com.Monarch.utils.JdbcUtils;


import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class Test1 {
    public static void main(String[] args) throws SQLException {
        Connection conn = JdbcUtils.getConnection();
        // 关闭自动提交，开启事务
        conn.setAutoCommit(false);

        // 事务内容
        String sql1 = "update account set money = money-100 where name = 'A'";
        PreparedStatement pst = conn.prepareStatement(sql1);
        pst.executeUpdate();

        String sql2 = "update account set money = money+100 where name = 'B'";
        pst = conn.prepareStatement(sql2);
        pst.executeUpdate();

        // 业务完毕，提交事务
        conn.commit();
        System.out.println("成功！！");

        JdbcUtils.release(conn, pst);
    }
}
