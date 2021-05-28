package Com.Monarch;

import Com.Monarch.utils.JdbcUtils_C3P0;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.text.ParseException;

public class TestC3P0 {
    public static void main(String[] args) throws SQLException, ParseException {
        Connection conn = JdbcUtils_C3P0.getConnection();
        String sql = "select * from users where id < ?";
        PreparedStatement pst = conn.prepareStatement(sql);

        pst.setInt(1, 3);

        ResultSet rs = pst.executeQuery();
        while (rs.next()){
            System.out.println(rs.getInt("id"));
            System.out.println(rs.getString("name"));
            System.out.println("=================");
        }

        JdbcUtils_C3P0.release(conn, pst, rs);
    }
}
