1、TCP SYN泛洪
在 SYN 洪水攻击（SYN flood attack）中，这会导致目标系统（通常是服务器）的 TCP 连接队列被填满，因为服务器会等待 SYN-ACK 的响应，并在其连接队列中为每个 SYN 数据包保持状态。如果攻击足够强烈，目标服务器可能会耗尽其连接队列资源，导致无法处理新的连接请求，这被称为拒绝服务攻击（Denial of Service, DoS）。
2. ICMP 洪水攻击（ICMP Flood Attack）
其目的是通过发送大量的 ICMP 数据包来消耗目标系统的资源，可能导致系统性能下降或完全不可用。
3.udp洪水攻击
UDP是一种无连接、无对话的网络协议，不需要像TCP那样进行三次握手，攻击者会发送大量伪造的UDP数据包到目标主机的随机端口，试图耗尽目标主机的资源。

hping3 是一款功能强大的命令行工具，用于生成和解析 TCP/IP 协议数据包。以下是一些常用的 hping3 参数：12
-c --count：发送数据包的数目。
-i --interval：发送数据包间隔的时间，可以是秒或微秒，例如 -i u1000 表示每秒发送1000个包。
-D --debug：开启调试模式。
-q --quiet：静默模式，只显示最后的统计数据。
-I --interface：选择特定的网卡接口。
-V --verbose：开启详细格式输出。
-n --numeric：数字化输出，象征性输出主机地址。
-z --bind：将 ctrl+z 组合键与 TTL 值绑定，按一次 TTL 值加 1。
-Z --unbind：取消绑定 ctrl+z 键。
-1 --icmp：ICMP 模式，发送 ICMP 应答包。
-2 --udp：UDP 模式，默认发送 UDP 报文到主机的 0 端口。
-8 --scan：扫描模式，扫描指定的端口。
-9 --listen：监听模式。
-a --spoof：源地址欺骗，伪造自身 IP 地址。
-t --ttl：指定 TTL 值（默认 64）。
-N --id：指定 ID 值（默认为随机值）。
-W --winid：使用 Windows 风格的 ID 字节顺序。
-r --rel：相对 ID 字段。
-f --frag：将数据包拆分成更多的分段。
-x --morefrag：设置更多的分段标志。
