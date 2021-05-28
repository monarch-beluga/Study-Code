package Com.Monarch;

import Com.Monarch.utils.JdbcUtils;

import java.sql.*;

public class SqlInjection {
    public static void main(String[] args) throws SQLException {
        // loginP("''or 1 = 1", "'' or 1 = 1");
        loginP("白鲸", "123456");
        // login("'or '1 = 1", "' or ' 1 = 1");
    }

    public static void login(String username, String password) throws SQLException {
        Connection conn = JdbcUtils.getConnection();
        Statement st = conn.createStatement();

        String sql = "select * from users where name='"+username+"' and password='"+password+"'";
        ResultSet rs = st.executeQuery(sql);
        while (rs.next()){
            System.out.println(rs.getString("name"));
            System.out.println(rs.getString("password"));
        }

        JdbcUtils.release(conn, st, rs);
    }

    public static void loginP(String username, String password) throws SQLException {
        Connection conn = JdbcUtils.getConnection();
        String sql = "select *  from users where name=? and password=?";
        PreparedStatement pst = conn.prepareStatement(sql);            // 预编译SQL

        pst.setString(1, username);
        pst.setString(2, password);

        ResultSet rs = pst.executeQuery();
        while (rs.next()){
            System.out.println(rs.getString("name"));
            System.out.println(rs.getString("password"));
        }
        JdbcUtils.release(conn, pst, rs);                    // 释放资源
    }
}
