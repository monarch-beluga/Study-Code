package Com.Monarch.utils;

import com.mchange.v2.c3p0.ComboPooledDataSource;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class JdbcUtils_C3P0 {

    private static final ComboPooledDataSource dataSource;

    static {
        // 将配置文件放入src目录下，c3p0会自动识别配置文件
        // 创建数据源
        dataSource = new ComboPooledDataSource();
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
