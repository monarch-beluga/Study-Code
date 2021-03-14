package Com.Monarch.Operation;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetSocketAddress;
import java.net.SocketException;
import java.util.Vector;

public class Client {
    public static void main(String[] args) {
        new ClientJFrame().init();
    }
}

class ClientJFrame extends JFrame{
    public void init(){
        loadPanel();
        setJFame();
    }
    public void setJFame(){
        setTitle("客户端");
        loadPanel();
        setVisible(true);
        setBounds(100,100,800,600);
        setResizable(false);
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
    }
    public void loadPanel(){
        add(new ClientJPanel());
    }
}
class ClientJPanel extends JPanel{
    private JTextField fieldUname, fieldIP, fieldSend;
    private Vector<String> textVector, userVector;
    private JList<String> textJList, userJList;
    private DatagramSocket socket;

    public void startSocket(int formPort) throws SocketException {
        socket = new DatagramSocket(formPort);
    }
    public void closeSocket(){
        socket.close();
    }

    public ClientJPanel() {
        setLayout(null);
        loadLabel();
        loadText();
        loadList();
        loadJButton();
    }
    public void loadLabel(){
        ClientLabel labelIp = new ClientLabel("IP");
        ClientLabel labelName = new ClientLabel("uname");
        ClientLabel labelList = new ClientLabel("用户列表");
        ClientLabel labelChat = new ClientLabel("聊天框");
        labelIp.setBounds(20, 20, 20, 15);
        labelName.setBounds(350, 20, 40, 15);
        labelList.setBounds(40, 50, 80, 15);
        labelChat.setBounds(200, 50, 80, 15);

        add(labelIp);
        add(labelName);
        add(labelList);
        add(labelChat);
    }
    public void loadText(){
        fieldIP = new JTextField();
        fieldIP.setFont(new Font("楷体", Font.PLAIN, 15));
        fieldIP.setHorizontalAlignment(JTextField.CENTER);
        fieldIP.setBounds(40, 15,300, 25);
        add(fieldIP);

        fieldUname = new JTextField();
        fieldUname.setFont(new Font("楷体", Font.PLAIN, 15));
        fieldUname.setHorizontalAlignment(JTextField.CENTER);
        fieldUname.setBounds(400, 15,200, 25);
        add(fieldUname);

        fieldSend = new JTextField();
        fieldSend.setFont(new Font("楷体",Font.PLAIN,20));
        fieldSend.setBounds(200,525,470,30);
        add(fieldSend);
    }
    public void loadList(){
        userVector = new Vector<>();
        userJList = new JList<>(userVector);
        userJList.setBounds(5,5,140,410);

        JPanel panel = new JPanel(null);
        panel.setBounds(20,80,150,420);
        panel.add(userJList);
        panel.setBackground(new Color(0x42423D));
        add(panel);

        textVector = new Vector<>();
        textJList = new JList<>(textVector);
        textJList.setFont(new Font("楷体",Font.PLAIN,15));
        JScrollPane scrollPane = new JScrollPane(textJList);
        scrollPane.setBounds(200,80, 550, 420);
        add(scrollPane);

    }
    public void loadJButton(){
        ClientButton buttonStart = new ClientButton("开始",610,15, 30);
        ClientButton buttonEnd = new ClientButton("结束",690,15, 30);
        ClientButton buttonSend = new ClientButton("发送", 690,520,40);

        buttonStart.setBackground(Color.GRAY);
        buttonEnd.setBackground(Color.GRAY);
        buttonSend.setBackground(Color.CYAN);

        ButtonActionListener listener = new ButtonActionListener();
        buttonStart.addActionListener(listener);
        buttonSend.addActionListener(listener);

        add(buttonStart);
        add(buttonEnd);
        add(buttonSend);
    }

    class ButtonActionListener implements ActionListener{
        private TalkSend talkSend;

        @Override
        public void actionPerformed(ActionEvent e) {
            String command = e.getActionCommand();
            if (command.equals("开始")){
                int fromPort = new Integer(fieldUname.getText().split(":")[1]);
                String uname = fieldUname.getText().split(":")[0];
                String toIp = fieldIP.getText().split(":")[0];
                int toPort = new Integer(fieldIP.getText().split(":")[1]);
                try {
                    startSocket(fromPort);
                    talkSend = new TalkSend(toIp,toPort);
                } catch (SocketException socketException) {
                    socketException.printStackTrace();
                }
                System.out.println(fieldUname.getText());
            }else if (command.equals("发送")){
                textVector.add(fieldSend.getText());
                textJList.setListData(textVector);
                fieldSend.setText("");
            }
        }
    }
    class TalkReceive implements Runnable{
        private final String msgFrom;
        private boolean flag = false;

        public TalkReceive(String msgFrom) throws SocketException {
            this.msgFrom = msgFrom;
        }

        @Override
        public void run() {
            while (true) {
                byte[] osBytes = new byte[1024];
                DatagramPacket osPacket = new DatagramPacket(osBytes, 0, osBytes.length);
                try {
                    socket.receive(osPacket);
                } catch (IOException e) {
                    e.printStackTrace();
                }
                String os = new String(osPacket.getData(), 0, osPacket.getLength());
                textVector.add("我：" +os);
                textJList.setListData(textVector);
                if (flag)
                    break;
            }
        }
        public void socketClose(){
            flag = true;
        }
    }
    class TalkSend implements Runnable{

        private final String toIP;
        private boolean flag = false;
        private boolean sendFlag = true;
        private final int toPort;
        private String is;

        public TalkSend(String toIP, int toPort){
            this.toIP = toIP;
            this.toPort = toPort;
        }
        public void getIs(String is){
            this.is = is;
        }

        @Override
        public void run() {
            while (true) {
                if (sendFlag) {
                    try {
                        wait();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
                byte[] isBytes = is.getBytes();
                DatagramPacket isPacket = new DatagramPacket(isBytes, 0, isBytes.length, new InetSocketAddress(toIP, toPort));
                try {
                    socket.send(isPacket);
                } catch (IOException e) {
                    e.printStackTrace();
                }
                if (flag){
                    break;
                }
                this.sendFlag = true;
            }
        }
        public void startSend(){
            sendFlag = false;
            this.notify();
        }
        public void socketClose(){
            flag = true;
        }
    }
}
class ClientLabel extends JLabel{
    public ClientLabel(String text) {
        super(text);
        setFont(new Font("楷体", Font.PLAIN, 15));
    }
}
class ClientButton extends JButton{
    public ClientButton(String text, int x, int y, int w) {
        super(text);
        setFont(new Font("楷体", Font.PLAIN, 20));
        setBounds(x, y, 75, w);
    }
}


