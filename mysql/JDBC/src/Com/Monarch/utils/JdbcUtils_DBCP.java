package Com.Monarch.utils;

import org.apache.commons.dbcp2.BasicDataSourceFactory;

import javax.sql.DataSource;
import java.io.InputStream;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Properties;

public class JdbcUtils_DBCP {

    private static DataSource dataSource;

    static {
        InputStream in = JdbcUtils.class.getResourceAsStream("/dbcpconfig.properties");
        try {
            Properties properties = new Properties();
            properties.load(in);

            // 创建数据源  工厂模式--->创建
            dataSource = BasicDataSourceFactory.createDataSource(properties);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // 获取连接
    public static Connection getConnection() throws SQLException {
        return dataSource.getConnection();          // 从数据源中获取连接
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
