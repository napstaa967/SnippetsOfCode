
using System.Diagnostics;
using System.Runtime.InteropServices;

namespace UPlayTooMuch
{
    public partial class Form1 : Form
    {
        private async Task WaitForProcessesToLaunch()
        {
            Debug.WriteLine("pre pre");
            Process[] procs = { };
            while (procs.Length == 0)
            {
                Debug.WriteLine(Properties.Resources.processestxt);
                var processes = Properties.Resources.processestxt.Split("\n");
                Debug.WriteLine(processes);
                foreach (string processName in processes)
                {
                    Debug.WriteLine(processName);
                    procs = Process.GetProcessesByName(Path.GetFileNameWithoutExtension(processName));
                    await Task.Delay(100);
                    foreach (Process p in procs)
                    {
                        p.Kill();
                    }
                }
            }
        }
        public Form1()
        {
            InitializeComponent();
        }

        private async void Form1_Load(object sender, EventArgs e)
        {
            Debug.WriteLine("A");
            await WaitForProcessesToLaunch();
            this.WindowState = FormWindowState.Maximized;
            [DllImport("user32.dll")]
            static extern bool LockWorkStation();
            [DllImport("user32.dll")]
            static extern bool ExitWindowsEx(uint uFlags, uint dWReason);

            ExitWindowsEx(1, 4);
            await Task.Delay(3000);
            Process.Start("shutdown", "/s /t 0");
            this.Close();
        }
    }
}