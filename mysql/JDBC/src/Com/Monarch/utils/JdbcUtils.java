package Com.Monarch.utils;

import java.io.InputStream;
import java.sql.*;
import java.util.Properties;

public class JdbcUtils {
    private static String url;
    private static String username;
    private static String password;

    static {
        InputStream in = JdbcUtils.class.getResourceAsStream("/db.properties");
        try {
            // InputStreamReader inr = new InputStreamReader(in, "UTF_8");  // 转换编码
            Properties properties = new Properties();
            // properties.load(inr);
            properties.load(in);
            String driver = properties.getProperty("driver");
            url = properties.getProperty("url");
            username = properties.getProperty("username");
            password = properties.getProperty("password");

            // 1. 驱动激活
            Class.forName(driver);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // 获取数据库对象
    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(url, username, password);
    }

    // 资源释放
    public static void release(Connection conn, Statement st, ResultSet rs){
        try {
            if (rs != null)
                rs.close();
            if (st != null)
                st.close();
            if (conn != null)
                conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    // 资源释放多态
    public static void release(Connection conn, Statement st){
        try {
            if (st != null)
                st.close();
            if (conn != null)
                conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
