// ==============================================================
// JDBC密码硬编码 (应被 rule17: secrets-db-password-jdbc 检测)
// CWE-798: Hardcoded Credentials
// ==============================================================

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class TestJDBC {

    // --- 变体1: JDBC连接字符串密码 (核心规则匹配) ---
    public void unsafe_jdbc_password() {
        String url = "jdbc:mysql://localhost:3306/mydb?user=root&password=admin123";  // 触发 rule17
        try {
            Connection conn = DriverManager.getConnection(url);
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM users");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // --- 变体2: JDBC + Properties ---
    public void unsafe_jdbc_properties() {
        String url = "jdbc:mysql://192.168.1.100:3306/proddb?user=admin&password=P@ssw0rd!";  // 触发 rule17
        try {
            Connection conn = DriverManager.getConnection(url);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // --- 变体3: postgresql JDBC ---
    public void unsafe_postgres_jdbc() {
        String url = "jdbc:postgresql://db.example.com:5432/appdb?user=app&password=secret123";
        try {
            Connection conn = DriverManager.getConnection(url);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // --- 变体4: 多参数JDBC URL ---
    public void unsafe_jdbc_multi() {
        String host = "db.internal";
        String url = "jdbc:mysql://" + host + "/app?user=root&password=root";  // 触发 rule17
        try {
            Connection conn = DriverManager.getConnection(url);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // --- 变体5: 成员变量硬编码 ---
    private static final String JDBC_URL = "jdbc:mysql://localhost/mydb?user=sa&password=sa123";  // 触发 rule17

    public void unsafe_jdbc_static() {
        try {
            Connection conn = DriverManager.getConnection(JDBC_URL);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
