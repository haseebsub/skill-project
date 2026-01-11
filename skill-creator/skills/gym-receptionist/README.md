# Gym Receptionist Skill

A comprehensive gym receptionist assistant that manages attendance tracking, fee reminders, payment submissions, and membership administration. This skill transforms Claude into your expert gym front desk manager for seamless gym operations and member service.

## 🏋️ What This Skill Does

This skill provides complete gym administrative management including:

- **Attendance Management** - Track member check-ins, generate reports, and monitor usage patterns
- **Fee Tracking & Payment Management** - Monitor monthly fees, send payment reminders, and track payment history
- **Membership Administration** - Manage membership renewals, track member information, and handle upgrades/downgrades
- **Automated Reminders** - Send automated notifications for fees, renewals, and important dates
- **Reporting & Analytics** - Generate comprehensive reports on attendance, revenue, and gym performance

## 📋 Quick Start

### For Users
1. **Use the skill when you need:**
   - Member attendance tracking and reporting
   - Fee payment reminders and tracking
   - Membership renewal management
   - Gym administrative reports
   - Payment history and billing inquiries

2. **Example requests:**
   - "Track today's gym attendance and generate a report"
   - "Send payment reminders to members with fees due next week"
   - "Check which memberships are expiring this month"
   - "Generate a monthly financial report for the gym"
   - "Find all members with overdue payments"

### For Developers
The skill includes:

- **SKILL.md** - Main skill documentation and comprehensive gym management guidance
- **Scripts/** - Interactive tools for attendance and fee management
- **References/** - Detailed operational guides for gym management
- **Assets/** - Printable templates for daily logs and reporting

## 🛠️ Included Tools

### Scripts

#### `attendance_manager.py`
Complete gym attendance management system featuring:
- Member check-in/check-out tracking
- Daily and monthly attendance reports
- Peak hour analysis and usage patterns
- Member status and visit history
- CSV export functionality
- Current check-in monitoring

**Key Features:**
- Real-time attendance tracking
- Member registration and management
- Automated visit counting and duration tracking
- Peak usage analysis for staffing decisions
- Export capabilities for external analysis

**Usage:**
```bash
python scripts/attendance_manager.py
```

#### `fee_manager.py`
Comprehensive gym fee management system with:
- Membership fee plan registration
- Payment recording and tracking
- Automated reminder system
- Overdue payment identification
- Financial reporting and analysis
- Member balance inquiries

**Key Features:**
- Flexible billing cycles (monthly, quarterly, annual)
- Multiple payment method support
- Late fee calculation and management
- Automated reminder scheduling
- Financial reporting and export

**Usage:**
```bash
python scripts/fee_manager.py
```

### References

#### `attendance_management_guide.md`
Complete guide to gym attendance management including:
- Daily check-in/check-out procedures
- Electronic vs. manual tracking systems
- Data analysis and reporting methods
- Peak hour management strategies
- Equipment usage monitoring
- Special event attendance coordination
- Data security and privacy protocols

#### `fee_management_guide.md`
Comprehensive fee management guide covering:
- Fee structure development and pricing strategy
- Payment processing system setup
- Automated payment and billing cycles
- Late payment management and collection procedures
- Financial reporting and analysis
- Special payment arrangements and hardship programs

### Assets

#### `daily_attendance_log.txt`
Printable daily attendance tracking template with:
- Member check-in/check-out logs
- Guest tracking and fee collection
- Equipment issues reporting
- Member feedback/complaints log
- Daily summary and staff notes
- Revenue tracking by payment method

#### `fee_reminder_template.txt`
Complete fee reminder system with:
- Member fee tracking worksheet
- Reminder schedule management
- Payment history log
- Outstanding balance tracking
- Payment arrangement documentation
- Pre-written reminder templates (email/SMS)

#### `monthly_report_template.txt`
Comprehensive monthly gym report template featuring:
- Attendance statistics and trends
- Membership changes and breakdowns
- Daily and hourly usage patterns
- Revenue and expense tracking
- Payment statistics and overdue accounts
- Member feedback and equipment issues
- Goals and focus areas for next month

## 🎮 Using the Skill

### When to Use This Skill

Use this skill when users request:

- **Attendance Tracking**: "Generate today's attendance report"
- **Fee Management**: "Check for overdue payments and send reminders"
- **Membership Administration**: "Find expiring memberships this month"
- **Financial Reporting**: "Generate monthly revenue report"
- **Gym Operations**: "Track equipment usage and member feedback"

### Example Workflow

1. **User Request**: "I need to track gym attendance for this month and identify members with overdue fees."

2. **Skill Activation**: Claude uses the skill to:
   - Generate monthly attendance report with usage patterns
   - Identify peak hours and member visit trends
   - Check for overdue payments and calculate outstanding balances
   - Suggest automated reminder strategies

3. **Ongoing Support**: Users can continue to:
   - Monitor daily attendance in real-time
   - Track payment collections and revenue
   - Generate custom reports for management decisions
   - Manage member inquiries and account issues

## 📊 Skill Statistics

- **Total Lines of Code**: ~850 lines
- **Scripts**: 2 comprehensive management systems
- **References**: 2 detailed operational guides
- **Assets**: 3 printable templates for daily operations
- **Coverage**: Complete gym front desk management

## 🔧 Technical Details

### Dependencies
- Python 3.6+
- Standard library only (no external dependencies)
- JSON support for data persistence
- CSV support for data export

### File Structure
```
gym-receptionist/
├── SKILL.md                        # Main skill documentation
├── README.md                       # This file
├── scripts/
│   ├── attendance_manager.py       # Member attendance tracking system
│   └── fee_manager.py              # Payment and fee management system
├── references/
│   ├── attendance_management_guide.md # Attendance procedures and analysis
│   └── fee_management_guide.md     # Fee structure and payment management
└── assets/
    ├── daily_attendance_log.txt        # Daily front desk log template
    ├── fee_reminder_template.txt       # Fee tracking and reminder system
    └── monthly_report_template.txt     # Monthly operational report
```

### Integration Points
- **Direct API**: Users can run Python scripts for real-time management
- **Template System**: Printable templates for manual tracking
- **Data Export**: CSV export for integration with external systems
- **Automated Reminders**: Built-in notification system for member communication

## 🎯 Skill Benefits

### For Gym Owners/Managers
- **Streamlined Operations**: Automated attendance and fee tracking
- **Improved Cash Flow**: Proactive payment reminders and tracking
- **Data-Driven Decisions**: Comprehensive reporting and analytics
- **Member Retention**: Personalized service and timely communication

### For Front Desk Staff
- **Efficient Check-in Process**: Quick member verification and logging
- **Payment Management**: Easy payment recording and balance checking
- **Member Service**: Quick access to member history and preferences
- **Reporting Tools**: Simple report generation for management

### For Members
- **Convenient Service**: Fast check-in and payment processing
- **Clear Communication**: Automated reminders and status updates
- **Personalized Experience**: Staff access to member preferences
- **Account Management**: Easy payment tracking and balance inquiries

## 🚀 Future Enhancements

Potential improvements to consider:
- Mobile app integration for member self-service
- Biometric check-in systems for enhanced security
- Integration with accounting software
- Advanced analytics for predictive staffing
- Member portal for online payments and account management

## 📞 Support

For questions about using this skill:
1. Check the SKILL.md for detailed operational procedures
2. Review the reference guides for specific management scenarios
3. Use the provided scripts for real-time data management
4. Follow the templates for consistent daily operations

## 📝 License

This skill is provided under the terms specified in LICENSE.txt

---

**Transform your gym operations with professional-grade attendance tracking, automated fee management, and comprehensive reporting tools for exceptional member service and operational efficiency.**