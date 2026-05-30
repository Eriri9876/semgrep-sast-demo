// ==============================================================
// 安全的Java配置写法 (负样本 - 不应被JDBC密码规则误报)
// ==============================================================

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class SafeConfig {

    // --- 安全写法1: 从环境变量读取 ---
    public void safe_env_variable() {
        String host = System.getenv("DB_HOST");
        String user = System.getenv("DB_USER");
        String pass = System.getenv("DB_PASSWORD");
        String url = "jdbc:mysql://" + host + "/mydb?user=" + user + "&password=" + pass;
        try {
            Connection conn = DriverManager.getConnection(url);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // --- 安全写法2: 从配置文件读取 ---
    public void safe_config_file() {
        // 从 application.properties 或 application.yml 读取
        // Properties props = new Properties();
        // props.load(new FileInputStream("config.properties"));
        // String url = props.getProperty("db.url");
        // Connection conn = DriverManager.getConnection(url, props);
    }

    // --- 安全写法3: 使用连接池 (HikariCP) ---
    public void safe_connection_pool() {
        // HikariConfig config = new HikariConfig();
        // config.setJdbcUrl(System.getenv("DB_URL"));
        // config.setUsername(System.getenv("DB_USER"));
        // config.setPassword(System.getenv("DB_PASS"));
        // HikariDataSource ds = new HikariDataSource(config);
    }

    // --- 安全写法4: 使用 Secret Manager ---
    public void safe_secret_manager() {
        // 从 AWS Secrets Manager / HashiCorp Vault 读取密码
        // String password = secretsManager.getSecret("db-password");
    }

    // --- 安全写法5: 参数化配置 ---
    public static Connection safe_parameterized(String host, String db, String user, String pass) {
        String url = "jdbc:mysql://" + host + "/" + db;
        try {
            return DriverManager.getConnection(url, user, pass);  // 参数传入，非硬编码
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
